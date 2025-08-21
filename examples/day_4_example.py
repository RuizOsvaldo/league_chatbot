"""
Day 4 Example: Database-Powered Chatbot
The LEAGUE of Amazing Programmers

Save conversations permanently with SQLite database!
Run: streamlit run day_4_example.py
"""

import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime
import json

# Page setup
st.set_page_config(
    page_title="Database Chatbot",
    page_icon="💾",
    layout="wide"
)

st.title("💾 Day 4: Chatbot with Database Memory")
st.write("Your bot now remembers everything - even after you close the app!")

# Database functions
def init_database():
    """Initialize the database with tables"""
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    
    # Create messages table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            sentiment TEXT,
            topic TEXT
        )
    ''')
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            total_messages INTEGER DEFAULT 0,
            favorite_topic TEXT,
            last_seen DATETIME
        )
    ''')
    
    # Create bot_responses table for custom responses
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bot_responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            trigger_word TEXT NOT NULL,
            response TEXT NOT NULL,
            usage_count INTEGER DEFAULT 0,
            created_by TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Add some default bot responses if table is empty
    cursor.execute("SELECT COUNT(*) FROM bot_responses")
    if cursor.fetchone()[0] == 0:
        default_responses = [
            ('hello', 'Hey there! Welcome back! I remember all our conversations! 👋'),
            ('help', 'I can chat, remember our past conversations, and learn new responses! Try teaching me something!'),
            ('database', 'Yes! I use SQLite to remember everything! Check the History tab to see our past chats! 💾'),
            ('forget', "I never forget! Everything is saved in my database! But you can delete specific messages if you want."),
            ('teach', 'You can teach me new responses! Just use the Teaching tab!')
        ]
        cursor.executemany(
            'INSERT INTO bot_responses (trigger_word, response) VALUES (?, ?)',
            default_responses
        )
    
    conn.commit()
    conn.close()

def save_message(session_id, role, content, sentiment=None, topic=None):
    """Save a message to the database"""
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO messages (session_id, role, content, sentiment, topic)
        VALUES (?, ?, ?, ?, ?)
    ''', (session_id, role, content, sentiment, topic))
    conn.commit()
    conn.close()

def get_conversation_history(session_id=None, limit=50):
    """Get conversation history from database"""
    conn = sqlite3.connect('chatbot.db')
    
    if session_id:
        query = '''
            SELECT role, content, timestamp, sentiment, topic 
            FROM messages 
            WHERE session_id = ?
            ORDER BY timestamp DESC 
            LIMIT ?
        '''
        df = pd.read_sql_query(query, conn, params=(session_id, limit))
    else:
        query = '''
            SELECT session_id, role, content, timestamp, sentiment, topic 
            FROM messages 
            ORDER BY timestamp DESC 
            LIMIT ?
        '''
        df = pd.read_sql_query(query, conn, params=(limit,))
    
    conn.close()
    return df

def get_user_stats(username):
    """Get user statistics from database"""
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    
    # Update last seen
    cursor.execute('''
        UPDATE users SET last_seen = CURRENT_TIMESTAMP 
        WHERE username = ?
    ''', (username,))
    
    # Get stats
    cursor.execute('''
        SELECT total_messages, favorite_topic, created_at, last_seen
        FROM users WHERE username = ?
    ''', (username,))
    
    result = cursor.fetchone()
    conn.commit()
    conn.close()
    
    return result

def create_or_update_user(username):
    """Create or update user in database"""
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT OR IGNORE INTO users (username, last_seen)
        VALUES (?, CURRENT_TIMESTAMP)
    ''', (username,))
    
    cursor.execute('''
        UPDATE users 
        SET total_messages = total_messages + 1, last_seen = CURRENT_TIMESTAMP
        WHERE username = ?
    ''', (username,))
    
    conn.commit()
    conn.close()

def get_bot_response_from_db(user_input):
    """Get bot response from database based on triggers"""
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    
    user_input_lower = user_input.lower()
    
    # Look for matching triggers
    cursor.execute('SELECT trigger_word, response FROM bot_responses')
    responses = cursor.fetchall()
    
    for trigger, response in responses:
        if trigger.lower() in user_input_lower:
            # Update usage count
            cursor.execute('''
                UPDATE bot_responses 
                SET usage_count = usage_count + 1 
                WHERE trigger_word = ?
            ''', (trigger,))
            conn.commit()
            conn.close()
            return response
    
    conn.close()
    return None

def add_custom_response(trigger, response, created_by="user"):
    """Add a custom bot response to database"""
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO bot_responses (trigger_word, response, created_by)
        VALUES (?, ?, ?)
    ''', (trigger, response, created_by))
    
    conn.commit()
    conn.close()

def get_database_stats():
    """Get overall database statistics"""
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    
    stats = {}
    
    # Total messages
    cursor.execute("SELECT COUNT(*) FROM messages")
    stats['total_messages'] = cursor.fetchone()[0]
    
    # Total users
    cursor.execute("SELECT COUNT(*) FROM users")
    stats['total_users'] = cursor.fetchone()[0]
    
    # Total custom responses
    cursor.execute("SELECT COUNT(*) FROM bot_responses")
    stats['total_responses'] = cursor.fetchone()[0]
    
    # Most active user
    cursor.execute('''
        SELECT username, total_messages 
        FROM users 
        ORDER BY total_messages DESC 
        LIMIT 1
    ''')
    result = cursor.fetchone()
    if result:
        stats['most_active_user'] = result[0]
        stats['most_active_messages'] = result[1]
    
    conn.close()
    return stats

# Initialize database
init_database()

# Session state initialization
if 'session_id' not in st.session_state:
    st.session_state.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")

if 'current_user' not in st.session_state:
    st.session_state.current_user = None

if 'messages' not in st.session_state:
    st.session_state.messages = []

# Sidebar - User login and stats
st.sidebar.header("👤 User Profile")

if not st.session_state.current_user:
    username = st.sidebar.text_input("Enter your username:")
    if st.sidebar.button("Login/Register"):
        if username:
            st.session_state.current_user = username
            create_or_update_user(username)
            st.rerun()
else:
    st.sidebar.success(f"Logged in as: {st.session_state.current_user}")
    
    # Show user stats
    user_stats = get_user_stats(st.session_state.current_user)
    if user_stats:
        st.sidebar.metric("Your Total Messages", user_stats[0])
        if user_stats[2]:
            st.sidebar.write(f"Member since: {user_stats[2][:10]}")
    
    if st.sidebar.button("Logout"):
        st.session_state.current_user = None
        st.session_state.messages = []
        st.rerun()

# Database stats in sidebar
st.sidebar.markdown("---")
st.sidebar.header("💾 Database Stats")
db_stats = get_database_stats()
st.sidebar.metric("Total Messages", db_stats['total_messages'])
st.sidebar.metric("Total Users", db_stats['total_users'])
st.sidebar.metric("Custom Responses", db_stats['total_responses'])

if 'most_active_user' in db_stats:
    st.sidebar.write(f"**Most Active**: {db_stats['most_active_user']} ({db_stats['most_active_messages']} messages)")

# Main interface with tabs
tab1, tab2, tab3, tab4 = st.tabs(["💬 Chat", "📜 History", "🎓 Teaching", "🔍 Search"])

with tab1:
    st.header("Chat with Database Memory")
    
    if not st.session_state.current_user:
        st.warning("Please login in the sidebar to start chatting!")
    else:
        # Load recent messages for this session
        if not st.session_state.messages:
            recent = get_conversation_history(st.session_state.session_id, 10)
            if not recent.empty:
                for _, row in recent.iterrows():
                    st.session_state.messages.append({
                        "role": row['role'],
                        "content": row['content']
                    })
        
        # Display messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])
        
        # Chat input
        if prompt := st.chat_input("Type your message..."):
            # Add user message
            st.session_state.messages.append({"role": "user", "content": prompt})
            save_message(st.session_state.session_id, "user", prompt)
            
            # Get bot response (check database first)
            bot_response = get_bot_response_from_db(prompt)
            
            if not bot_response:
                # Default responses if no database match
                if "history" in prompt.lower():
                    bot_response = "I can see all our past conversations! Check the History tab to explore them! 📜"
                elif "remember" in prompt.lower():
                    bot_response = f"I remember everything, {st.session_state.current_user}! Our conversations are safely stored in my database! 🧠"
                elif "teach" in prompt.lower():
                    bot_response = "You can teach me new responses in the Teaching tab! I love learning! 🎓"
                else:
                    bot_response = f"Thanks for sharing that, {st.session_state.current_user}! I've saved it to my memory! 💾"
            
            # Add and save bot response
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
            save_message(st.session_state.session_id, "assistant", bot_response)
            
            # Update user message count
            create_or_update_user(st.session_state.current_user)
            
            st.rerun()

with tab2:
    st.header("📜 Conversation History")
    
    # Filter options
    col1, col2 = st.columns(2)
    with col1:
        show_all = st.checkbox("Show all sessions", value=False)
    with col2:
        limit = st.selectbox("Messages to show:", [10, 25, 50, 100], index=1)
    
    # Get and display history
    if show_all:
        history = get_conversation_history(limit=limit)
    else:
        history = get_conversation_history(st.session_state.session_id, limit)
    
    if not history.empty:
        # Display as a nice table
        st.dataframe(
            history[['timestamp', 'role', 'content']].sort_values('timestamp', ascending=False),
            use_container_width=True,
            hide_index=True
        )
        
        # Export option
        if st.button("📥 Export History as CSV"):
            csv = history.to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name=f"chat_history_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )
    else:
        st.info("No conversation history yet. Start chatting to build your history!")

with tab3:
    st.header("🎓 Teach Your Bot")
    st.write("Add custom responses to make your bot smarter!")
    
    with st.form("teach_bot"):
        trigger = st.text_input("When someone says (trigger word/phrase):")
        response = st.text_area("The bot should respond with:")
        
        if st.form_submit_button("Teach Bot"):
            if trigger and response:
                add_custom_response(trigger, response, st.session_state.current_user or "anonymous")
                st.success(f"✅ Taught the bot to respond to '{trigger}'!")
                st.balloons()
            else:
                st.error("Please provide both a trigger and a response!")
    
    # Show existing custom responses
    st.subheader("Current Custom Responses")
    conn = sqlite3.connect('chatbot.db')
    responses_df = pd.read_sql_query(
        "SELECT trigger_word, response, usage_count, created_by FROM bot_responses ORDER BY usage_count DESC",
        conn
    )
    conn.close()
    
    if not responses_df.empty:
        st.dataframe(responses_df, use_container_width=True, hide_index=True)

with tab4:
    st.header("🔍 Search Conversations")
    
    search_term = st.text_input("Search for messages containing:")
    
    if search_term:
        conn = sqlite3.connect('chatbot.db')
        search_query = '''
            SELECT role, content, timestamp 
            FROM messages 
            WHERE content LIKE ? 
            ORDER BY timestamp DESC 
            LIMIT 20
        '''
        results = pd.read_sql_query(search_query, conn, params=(f'%{search_term}%',))
        conn.close()
        
        if not results.empty:
            st.success(f"Found {len(results)} messages containing '{search_term}'")
            st.dataframe(results, use_container_width=True, hide_index=True)
        else:
            st.info(f"No messages found containing '{search_term}'")

# Footer
st.markdown("---")
st.success("""
**🎯 Day 4 Challenge**: Can you add these database features?
- Track conversation topics and show most discussed topics
- Add a "favorite messages" feature
- Create user profiles with preferences
- Build a message deletion system
""")

"""
🚀 Tomorrow: We'll add advanced features like games, quizzes, and special commands!
"""