"""
Day 6 Example: Final Polish & Deployment Ready Chatbot
The LEAGUE of Amazing Programmers

Polish your chatbot and prepare for deployment!
Run: streamlit run day_6_example.py
"""

import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random
import json
import hashlib

# Professional page configuration
st.set_page_config(
    page_title="My Amazing Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://docs.streamlit.io',
        'Report a bug': 'mailto:your-email@example.com',
        'About': "# My Amazing Chatbot v1.0\nBuilt with ❤️ using Streamlit"
    }
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 1rem;
    }
    .stat-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .achievement-badge {
        background: gold;
        color: black;
        padding: 0.5rem;
        border-radius: 20px;
        display: inline-block;
        margin: 0.2rem;
    }
</style>
""", unsafe_allow_html=True)

# Enhanced database with all features
@st.cache_resource
def init_complete_database():
    """Initialize complete database with all tables"""
    conn = sqlite3.connect('chatbot_final.db')
    cursor = conn.cursor()
    
    # Complete messages table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT,
            user_id TEXT,
            role TEXT,
            content TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            sentiment TEXT,
            topic TEXT,
            rating INTEGER
        )
    ''')
    
    # User profiles with preferences
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_profiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            display_name TEXT,
            avatar TEXT,
            bio TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            last_seen DATETIME,
            total_messages INTEGER DEFAULT 0,
            total_score INTEGER DEFAULT 0,
            preferences TEXT,
            theme TEXT DEFAULT 'default'
        )
    ''')
    
    # Enhanced game scores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS game_scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            game_type TEXT,
            score INTEGER,
            difficulty TEXT,
            duration INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Bot personalities
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bot_personalities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            description TEXT,
            response_style TEXT,
            emoji_set TEXT,
            created_by TEXT,
            is_active BOOLEAN DEFAULT 0
        )
    ''')
    
    # Add default personalities if empty
    cursor.execute("SELECT COUNT(*) FROM bot_personalities")
    if cursor.fetchone()[0] == 0:
        personalities = [
            ('Friendly', 'Warm and helpful assistant', 'casual', '😊🎉👋💫', 'system'),
            ('Professional', 'Formal and informative', 'formal', '📊💼📈🎯', 'system'),
            ('Gamer', 'Gaming enthusiast buddy', 'gaming', '🎮🕹️👾🏆', 'system'),
            ('Teacher', 'Educational and patient', 'educational', '📚🎓💡✏️', 'system'),
            ('Comedian', 'Always ready with jokes', 'humorous', '😄🤣🎭🃏', 'system')
        ]
        cursor.executemany(
            'INSERT INTO bot_personalities (name, description, response_style, emoji_set, created_by) VALUES (?, ?, ?, ?, ?)',
            personalities
        )
        # Set Friendly as default
        cursor.execute("UPDATE bot_personalities SET is_active = 1 WHERE name = 'Friendly'")
    
    conn.commit()
    conn.close()

# Initialize database
init_complete_database()

# Session state initialization with all features
if 'session_id' not in st.session_state:
    st.session_state.session_id = hashlib.md5(str(datetime.now()).encode()).hexdigest()[:8]

if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'user_profile' not in st.session_state:
    st.session_state.user_profile = None

if 'bot_personality' not in st.session_state:
    st.session_state.bot_personality = 'Friendly'

if 'app_settings' not in st.session_state:
    st.session_state.app_settings = {
        'dark_mode': False,
        'sound_effects': True,
        'auto_save': True,
        'show_timestamps': True,
        'message_limit': 100
    }

# Cached functions for performance
@st.cache_data(ttl=60)
def get_user_statistics(username):
    """Get cached user statistics"""
    conn = sqlite3.connect('chatbot_final.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT total_messages, total_score, created_at, last_seen
        FROM user_profiles WHERE username = ?
    ''', (username,))
    
    stats = cursor.fetchone()
    conn.close()
    return stats

@st.cache_data(ttl=30)
def get_leaderboard():
    """Get cached leaderboard data"""
    conn = sqlite3.connect('chatbot_final.db')
    query = '''
        SELECT username, total_score, total_messages
        FROM user_profiles
        ORDER BY total_score DESC
        LIMIT 10
    '''
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def create_or_login_user(username, display_name=None):
    """Create or login user with profile"""
    conn = sqlite3.connect('chatbot_final.db')
    cursor = conn.cursor()
    
    # Check if user exists
    cursor.execute('SELECT * FROM user_profiles WHERE username = ?', (username,))
    user = cursor.fetchone()
    
    if not user:
        # Create new user
        cursor.execute('''
            INSERT INTO user_profiles (username, display_name)
            VALUES (?, ?)
        ''', (username, display_name or username))
        st.balloons()
        welcome_msg = f"🎉 Welcome {username}! Your profile has been created!"
    else:
        # Update last seen
        cursor.execute('''
            UPDATE user_profiles 
            SET last_seen = CURRENT_TIMESTAMP
            WHERE username = ?
        ''', (username,))
        welcome_msg = f"👋 Welcome back, {username}!"
    
    conn.commit()
    conn.close()
    return welcome_msg

def get_personality_response(user_input, personality):
    """Get response based on bot personality"""
    conn = sqlite3.connect('chatbot_final.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT response_style, emoji_set 
        FROM bot_personalities 
        WHERE name = ?
    ''', (personality,))
    
    style_data = cursor.fetchone()
    conn.close()
    
    if not style_data:
        return "Hello! How can I help you today?"
    
    style, emojis = style_data
    emoji_list = emojis.split()
    
    # Generate response based on personality
    responses = {
        'casual': [
            f"Hey! That's cool! {random.choice(emoji_list)}",
            f"Awesome! Tell me more! {random.choice(emoji_list)}",
            f"No way! That's interesting! {random.choice(emoji_list)}"
        ],
        'formal': [
            f"I understand. Please continue. {random.choice(emoji_list)}",
            f"Thank you for sharing that information. {random.choice(emoji_list)}",
            f"That's quite insightful. {random.choice(emoji_list)}"
        ],
        'gaming': [
            f"GG! That's epic! {random.choice(emoji_list)}",
            f"Nice move, player! {random.choice(emoji_list)}",
            f"Level up! You're crushing it! {random.choice(emoji_list)}"
        ],
        'educational': [
            f"Excellent observation! {random.choice(emoji_list)}",
            f"That's a great learning opportunity! {random.choice(emoji_list)}",
            f"Let me explain further... {random.choice(emoji_list)}"
        ],
        'humorous': [
            f"Haha! You're hilarious! {random.choice(emoji_list)}",
            f"That reminds me of a joke... {random.choice(emoji_list)}",
            f"LOL! You've got great timing! {random.choice(emoji_list)}"
        ]
    }
    
    return random.choice(responses.get(style, ["Interesting!"]))

# Main app header
st.markdown('<h1 class="main-header">🤖 My Amazing Chatbot</h1>', unsafe_allow_html=True)

# Sidebar with complete features
with st.sidebar:
    st.header("👤 User Profile")
    
    if not st.session_state.user_profile:
        with st.form("login_form"):
            username = st.text_input("Username:")
            display_name = st.text_input("Display Name (optional):")
            
            if st.form_submit_button("Login / Sign Up", type="primary"):
                if username:
                    welcome_msg = create_or_login_user(username, display_name)
                    st.session_state.user_profile = username
                    st.success(welcome_msg)
                    st.rerun()
    else:
        # Show user stats
        stats = get_user_statistics(st.session_state.user_profile)
        if stats:
            st.success(f"Logged in as: **{st.session_state.user_profile}**")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Messages", stats[0])
            with col2:
                st.metric("Score", stats[1])
            
            st.caption(f"Member since: {stats[2][:10]}")
            
            if st.button("Logout"):
                st.session_state.user_profile = None
                st.session_state.messages = []
                st.rerun()
    
    st.markdown("---")
    
    # Bot personality selector
    st.header("🎭 Bot Personality")
    conn = sqlite3.connect('chatbot_final.db')
    personalities_df = pd.read_sql_query(
        "SELECT name, description FROM bot_personalities",
        conn
    )
    conn.close()
    
    personality = st.selectbox(
        "Choose personality:",
        personalities_df['name'].tolist(),
        index=0
    )
    
    if personality != st.session_state.bot_personality:
        st.session_state.bot_personality = personality
        st.rerun()
    
    # Show personality description
    desc = personalities_df[personalities_df['name'] == personality]['description'].values[0]
    st.caption(desc)
    
    st.markdown("---")
    
    # App settings
    with st.expander("⚙️ Settings"):
        st.session_state.app_settings['show_timestamps'] = st.checkbox(
            "Show timestamps",
            value=st.session_state.app_settings['show_timestamps']
        )
        st.session_state.app_settings['sound_effects'] = st.checkbox(
            "Sound effects",
            value=st.session_state.app_settings['sound_effects']
        )
        st.session_state.app_settings['auto_save'] = st.checkbox(
            "Auto-save conversations",
            value=st.session_state.app_settings['auto_save']
        )

# Main content area with tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "💬 Chat", "📊 Analytics", "🏆 Leaderboard", "🎮 Games", "📚 Help"
])

with tab1:
    # Chat interface
    if not st.session_state.user_profile:
        st.info("👈 Please login in the sidebar to start chatting!")
    else:
        # Welcome message if no messages
        if not st.session_state.messages:
            welcome = f"Welcome {st.session_state.user_profile}! I'm using the {st.session_state.bot_personality} personality. How can I help you today?"
            st.session_state.messages.append({
                "role": "assistant",
                "content": welcome,
                "timestamp": datetime.now()
            })
        
        # Display messages
        for message in st.session_state.messages[-st.session_state.app_settings['message_limit']:]:
            with st.chat_message(message["role"]):
                st.write(message["content"])
                if st.session_state.app_settings['show_timestamps'] and 'timestamp' in message:
                    st.caption(message['timestamp'].strftime("%I:%M %p"))
        
        # Chat input
        if prompt := st.chat_input("Type your message..."):
            # Add user message
            st.session_state.messages.append({
                "role": "user",
                "content": prompt,
                "timestamp": datetime.now()
            })
            
            # Get bot response based on personality
            bot_response = get_personality_response(prompt, st.session_state.bot_personality)
            
            # Add bot response
            st.session_state.messages.append({
                "role": "assistant",
                "content": bot_response,
                "timestamp": datetime.now()
            })
            
            # Save to database if auto-save is on
            if st.session_state.app_settings['auto_save']:
                conn = sqlite3.connect('chatbot_final.db')
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO messages (session_id, user_id, role, content)
                    VALUES (?, ?, ?, ?)
                ''', (st.session_state.session_id, st.session_state.user_profile, "user", prompt))
                cursor.execute('''
                    INSERT INTO messages (session_id, user_id, role, content)
                    VALUES (?, ?, ?, ?)
                ''', (st.session_state.session_id, st.session_state.user_profile, "assistant", bot_response))
                
                # Update user message count
                cursor.execute('''
                    UPDATE user_profiles 
                    SET total_messages = total_messages + 2
                    WHERE username = ?
                ''', (st.session_state.user_profile,))
                
                conn.commit()
                conn.close()
            
            st.rerun()

with tab2:
    st.header("📊 Chat Analytics")
    
    if st.session_state.user_profile:
        # Get user's message history
        conn = sqlite3.connect('chatbot_final.db')
        
        # Messages over time
        query = '''
            SELECT DATE(timestamp) as date, COUNT(*) as count
            FROM messages
            WHERE user_id = ?
            GROUP BY DATE(timestamp)
            ORDER BY date DESC
            LIMIT 7
        '''
        daily_messages = pd.read_sql_query(query, conn, params=(st.session_state.user_profile,))
        
        if not daily_messages.empty:
            col1, col2 = st.columns(2)
            
            with col1:
                # Daily message chart
                fig = px.bar(daily_messages, x='date', y='count',
                           title='Messages Per Day (Last 7 Days)',
                           labels={'count': 'Messages', 'date': 'Date'})
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                # Message distribution
                role_query = '''
                    SELECT role, COUNT(*) as count
                    FROM messages
                    WHERE user_id = ?
                    GROUP BY role
                '''
                role_dist = pd.read_sql_query(role_query, conn, params=(st.session_state.user_profile,))
                
                if not role_dist.empty:
                    fig = go.Figure(data=[go.Pie(
                        labels=role_dist['role'],
                        values=role_dist['count'],
                        hole=.3
                    )])
                    fig.update_layout(title="Message Distribution")
                    st.plotly_chart(fig, use_container_width=True)
            
            # Word frequency
            st.subheader("🔤 Your Most Used Words")
            words_query = '''
                SELECT content FROM messages
                WHERE user_id = ? AND role = 'user'
                LIMIT 100
            '''
            user_messages = pd.read_sql_query(words_query, conn, params=(st.session_state.user_profile,))
            
            if not user_messages.empty:
                # Simple word frequency analysis
                all_words = ' '.join(user_messages['content']).lower().split()
                word_freq = {}
                for word in all_words:
                    if len(word) > 4:  # Only count longer words
                        word_freq[word] = word_freq.get(word, 0) + 1
                
                # Top 10 words
                top_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]
                if top_words:
                    words_df = pd.DataFrame(top_words, columns=['Word', 'Count'])
                    fig = px.bar(words_df, x='Count', y='Word', orientation='h',
                               title="Your Top 10 Words")
                    st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Start chatting to see your analytics!")
        
        conn.close()
    else:
        st.info("Login to see your chat analytics!")

with tab3:
    st.header("🏆 Global Leaderboard")
    
    leaderboard = get_leaderboard()
    
    if not leaderboard.empty:
        # Display leaderboard with medals
        for idx, row in leaderboard.iterrows():
            medal = ""
            if idx == 0:
                medal = "🥇"
            elif idx == 1:
                medal = "🥈"
            elif idx == 2:
                medal = "🥉"
            
            col1, col2, col3, col4 = st.columns([1, 3, 2, 2])
            with col1:
                st.write(f"{medal} #{idx + 1}")
            with col2:
                st.write(f"**{row['username']}**")
            with col3:
                st.write(f"Score: {row['total_score']}")
            with col4:
                st.write(f"Messages: {row['total_messages']}")
        
        # User's rank
        if st.session_state.user_profile:
            conn = sqlite3.connect('chatbot_final.db')
            cursor = conn.cursor()
            cursor.execute('''
                SELECT COUNT(*) + 1 as rank
                FROM user_profiles
                WHERE total_score > (
                    SELECT total_score FROM user_profiles WHERE username = ?
                )
            ''', (st.session_state.user_profile,))
            rank = cursor.fetchone()[0]
            conn.close()
            
            st.markdown("---")
            st.info(f"Your rank: #{rank}")
    else:
        st.info("No users yet! Be the first on the leaderboard!")

with tab4:
    st.header("🎮 Quick Games")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🎲 Dice Roll")
        if st.button("Roll Dice", use_container_width=True):
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            st.success(f"You rolled: {dice1} and {dice2} = **{dice1 + dice2}**")
            
            if dice1 == dice2:
                st.balloons()
                st.success("🎉 DOUBLES! +10 bonus points!")
                if st.session_state.user_profile:
                    conn = sqlite3.connect('chatbot_final.db')
                    cursor = conn.cursor()
                    cursor.execute('''
                        UPDATE user_profiles 
                        SET total_score = total_score + 10
                        WHERE username = ?
                    ''', (st.session_state.user_profile,))
                    conn.commit()
                    conn.close()
    
    with col2:
        st.subheader("🪙 Coin Flip")
        if st.button("Flip Coin", use_container_width=True):
            result = random.choice(['Heads', 'Tails'])
            if result == 'Heads':
                st.success("🪙 **HEADS**")
            else:
                st.info("🪙 **TAILS**")
    
    with col3:
        st.subheader("🎱 Magic 8-Ball")
        question = st.text_input("Ask a question:")
        if st.button("Ask 8-Ball", use_container_width=True):
            if question:
                responses = [
                    "Yes, definitely! ✨",
                    "Ask again later... 🔮",
                    "Cannot predict now 🌙",
                    "Don't count on it 😬",
                    "My sources say yes! 🌟",
                    "Very doubtful 🤔"
                ]
                st.info(f"🎱 {random.choice(responses)}")

with tab5:
    st.header("📚 Help & Documentation")
    
    with st.expander("🚀 Getting Started"):
        st.markdown("""
        ### Welcome to Your Chatbot!
        
        1. **Login**: Create a username in the sidebar
        2. **Choose Personality**: Select how you want the bot to behave
        3. **Start Chatting**: Type messages in the chat input
        4. **Play Games**: Check the Games tab for fun activities
        5. **Track Progress**: View your analytics and leaderboard rank
        """)
    
    with st.expander("🎮 Features"):
        st.markdown("""
        ### Available Features:
        
        - **Multiple Personalities**: Choose from Friendly, Professional, Gamer, Teacher, or Comedian
        - **Persistent Memory**: All conversations are saved
        - **Analytics Dashboard**: Track your chat patterns
        - **Global Leaderboard**: Compete with other users
        - **Quick Games**: Dice, coin flip, and magic 8-ball
        - **Auto-save**: Automatically save conversations
        - **Export Data**: Download your chat history
        """)
    
    with st.expander("🌐 Deployment Guide"):
        st.markdown("""
        ### Deploy Your Chatbot:
        
        1. **Streamlit Community Cloud** (Recommended):
           - Push your code to GitHub
           - Sign up at share.streamlit.io
           - Connect your GitHub repo
           - Click Deploy!
        
        2. **Requirements**:
           - Make sure you have requirements.txt
           - Include all dependencies
           - Test locally first
        
        3. **Database Note**:
           - SQLite works great for small apps
           - For production, consider PostgreSQL
        """)
    
    with st.expander("💡 Tips & Tricks"):
        st.markdown("""
        ### Pro Tips:
        
        - Use keyboard shortcuts (Enter to send)
        - Try different personalities for variety
        - Check analytics to see your patterns
        - Compete on the leaderboard
        - Export your data regularly
        - Customize the bot's responses
        """)

# Footer with app info
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.caption("🤖 Chatbot v1.0")

with col2:
    st.caption(f"📅 {datetime.now().strftime('%B %d, %Y')}")

with col3:
    if st.button("📥 Export Chat"):
        if st.session_state.messages:
            chat_data = {
                'session_id': st.session_state.session_id,
                'user': st.session_state.user_profile,
                'messages': [
                    {
                        'role': m['role'],
                        'content': m['content'],
                        'timestamp': m['timestamp'].isoformat() if 'timestamp' in m else None
                    }
                    for m in st.session_state.messages
                ],
                'exported_at': datetime.now().isoformat()
            }
            json_str = json.dumps(chat_data, indent=2)
            st.download_button(
                label="Download JSON",
                data=json_str,
                file_name=f"chat_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )

# Success message for deployment
st.success("""
**🎉 Your chatbot is deployment-ready!**
- Professional UI with custom styling
- Complete user system with profiles
- Multiple bot personalities
- Analytics and leaderboard
- Database persistence
- Export functionality
- Mobile-responsive design

**Next Steps:**
1. Push to GitHub
2. Deploy on Streamlit Community Cloud
3. Share with friends!
""")

"""
🚀 Congratulations! You've built a complete, professional chatbot application!
"""