"""
Day 3 Example: Chat Analytics & Beautiful Visualizations
The LEAGUE of Amazing Programmers

Add data visualization and analytics to your chatbot!
Run: streamlit run day_3_example.py
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random
import json

# Page setup
st.set_page_config(
    page_title="Analytics Chatbot",
    page_icon="📊",
    layout="wide"  # Wide layout for charts
)

st.title("📊 Day 3: Chatbot with Analytics Dashboard")
st.write("Track conversations, visualize patterns, and make data-driven improvements!")

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Welcome to the Analytics Bot! 📊 I track our conversation patterns. Try chatting with me and check the analytics tab!",
        "timestamp": datetime.now().isoformat(),
        "sentiment": "positive"
    })

if 'message_stats' not in st.session_state:
    st.session_state.message_stats = {
        'total_messages': 0,
        'user_messages': 0,
        'bot_messages': 1,
        'topics': {},
        'hourly_activity': {},
        'word_frequency': {},
        'response_times': [],
        'sentiment_scores': {'positive': 1, 'neutral': 0, 'negative': 0}
    }

if 'user_preferences' not in st.session_state:
    st.session_state.user_preferences = {
        'favorite_topic': None,
        'chat_style': 'friendly',
        'emoji_usage': True
    }

# Helper functions
def analyze_sentiment(text):
    """Simple sentiment analysis based on keywords"""
    positive_words = ['good', 'great', 'awesome', 'love', 'excellent', 'happy', 'wonderful', 'fantastic', 'amazing', 'yes', 'thanks']
    negative_words = ['bad', 'hate', 'terrible', 'awful', 'horrible', 'sad', 'angry', 'worst', 'no', 'never']
    
    text_lower = text.lower()
    positive_count = sum(1 for word in positive_words if word in text_lower)
    negative_count = sum(1 for word in negative_words if word in text_lower)
    
    if positive_count > negative_count:
        return 'positive'
    elif negative_count > positive_count:
        return 'negative'
    else:
        return 'neutral'

def detect_topic(text):
    """Detect conversation topics"""
    topics = {
        'tech': ['computer', 'code', 'program', 'app', 'software', 'tech', 'ai', 'robot'],
        'school': ['homework', 'class', 'teacher', 'study', 'exam', 'test', 'grade', 'school'],
        'gaming': ['game', 'play', 'video game', 'minecraft', 'fortnite', 'roblox', 'gaming'],
        'music': ['music', 'song', 'band', 'singer', 'playlist', 'spotify', 'concert'],
        'sports': ['sports', 'football', 'basketball', 'soccer', 'team', 'game', 'player'],
        'food': ['food', 'eat', 'hungry', 'lunch', 'dinner', 'pizza', 'burger', 'snack'],
        'general': []
    }
    
    text_lower = text.lower()
    for topic, keywords in topics.items():
        if any(keyword in text_lower for keyword in keywords):
            return topic
    return 'general'

def update_stats(message, role):
    """Update message statistics"""
    stats = st.session_state.message_stats
    
    # Update message counts
    stats['total_messages'] += 1
    if role == 'user':
        stats['user_messages'] += 1
    else:
        stats['bot_messages'] += 1
    
    # Track hourly activity
    hour = datetime.now().hour
    stats['hourly_activity'][hour] = stats['hourly_activity'].get(hour, 0) + 1
    
    # Track topics
    topic = detect_topic(message)
    stats['topics'][topic] = stats['topics'].get(topic, 0) + 1
    
    # Track word frequency
    words = message.lower().split()
    for word in words:
        if len(word) > 3:  # Only track words longer than 3 characters
            stats['word_frequency'][word] = stats['word_frequency'].get(word, 0) + 1
    
    # Track sentiment
    sentiment = analyze_sentiment(message)
    stats['sentiment_scores'][sentiment] = stats['sentiment_scores'].get(sentiment, 0) + 1

def get_smart_response(user_input):
    """Generate responses with analytics awareness"""
    responses = {
        'analytics': "I can see you're interested in the data! Check out the Analytics tab for cool visualizations! 📈",
        'positive': "You seem happy! That's awesome! Your positive vibes are making my charts go up! 😊",
        'negative': "I sense you might be frustrated. How can I help make things better? 🤗",
        'question': "Great question! I love curious minds! Let me think about that... 🤔",
        'greeting': "Hey there! Ready to generate some interesting conversation data? 👋",
        'default': "Interesting! That's going in my analytics! Want to see your conversation patterns? 📊"
    }
    
    user_input_lower = user_input.lower()
    
    if any(word in user_input_lower for word in ['analytics', 'data', 'stats', 'chart']):
        return responses['analytics']
    elif '?' in user_input:
        return responses['question']
    elif any(word in user_input_lower for word in ['hi', 'hello', 'hey']):
        return responses['greeting']
    elif analyze_sentiment(user_input) == 'positive':
        return responses['positive']
    elif analyze_sentiment(user_input) == 'negative':
        return responses['negative']
    else:
        return responses['default']

# Create tabs for chat and analytics
tab1, tab2, tab3 = st.tabs(["💬 Chat", "📊 Analytics", "⚙️ Settings"])

with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("Chat Interface")
        
        # Display chat messages
        chat_container = st.container()
        with chat_container:
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.write(message["content"])
                    if "timestamp" in message:
                        st.caption(f"Sent at {message['timestamp'][:19]}")
        
        # Chat input
        if prompt := st.chat_input("Type your message..."):
            # Add timestamp to user message
            timestamp = datetime.now().isoformat()
            sentiment = analyze_sentiment(prompt)
            
            # Add user message
            st.session_state.messages.append({
                "role": "user",
                "content": prompt,
                "timestamp": timestamp,
                "sentiment": sentiment
            })
            update_stats(prompt, "user")
            
            # Generate bot response
            bot_response = get_smart_response(prompt)
            bot_sentiment = analyze_sentiment(bot_response)
            
            # Add bot response
            st.session_state.messages.append({
                "role": "assistant",
                "content": bot_response,
                "timestamp": datetime.now().isoformat(),
                "sentiment": bot_sentiment
            })
            update_stats(bot_response, "assistant")
            
            st.rerun()
    
    with col2:
        st.header("Quick Stats")
        
        # Real-time metrics
        st.metric("Total Messages", st.session_state.message_stats['total_messages'])
        st.metric("Your Messages", st.session_state.message_stats['user_messages'])
        st.metric("Bot Messages", st.session_state.message_stats['bot_messages'])
        
        # Sentiment indicator
        sentiments = st.session_state.message_stats['sentiment_scores']
        total_sentiment = sum(sentiments.values())
        if total_sentiment > 0:
            positive_pct = (sentiments['positive'] / total_sentiment) * 100
            st.metric("Positive Vibes", f"{positive_pct:.0f}%")
        
        # Most discussed topic
        if st.session_state.message_stats['topics']:
            top_topic = max(st.session_state.message_stats['topics'].items(), key=lambda x: x[1])
            st.metric("Hot Topic", top_topic[0].capitalize())

with tab2:
    st.header("📊 Conversation Analytics")
    
    if st.session_state.message_stats['total_messages'] > 0:
        # Create visualizations
        col1, col2 = st.columns(2)
        
        with col1:
            # Message distribution pie chart
            fig_pie = go.Figure(data=[go.Pie(
                labels=['You', 'Bot'],
                values=[st.session_state.message_stats['user_messages'], 
                       st.session_state.message_stats['bot_messages']],
                hole=.3,
                marker_colors=['#FF6B6B', '#4ECDC4']
            )])
            fig_pie.update_layout(title="Message Distribution", height=300)
            st.plotly_chart(fig_pie, use_container_width=True)
            
            # Topic distribution
            if st.session_state.message_stats['topics']:
                topics_df = pd.DataFrame(
                    list(st.session_state.message_stats['topics'].items()),
                    columns=['Topic', 'Count']
                )
                fig_topics = px.bar(topics_df, x='Topic', y='Count', 
                                   title="Topics Discussed",
                                   color='Count', color_continuous_scale='viridis')
                fig_topics.update_layout(height=300)
                st.plotly_chart(fig_topics, use_container_width=True)
        
        with col2:
            # Sentiment analysis
            sentiment_df = pd.DataFrame(
                list(st.session_state.message_stats['sentiment_scores'].items()),
                columns=['Sentiment', 'Count']
            )
            fig_sentiment = px.bar(sentiment_df, x='Sentiment', y='Count',
                                  title="Conversation Sentiment",
                                  color='Sentiment',
                                  color_discrete_map={'positive': '#52C41A', 
                                                     'neutral': '#FAAD14', 
                                                     'negative': '#FF4D4F'})
            fig_sentiment.update_layout(height=300)
            st.plotly_chart(fig_sentiment, use_container_width=True)
            
            # Hourly activity
            if st.session_state.message_stats['hourly_activity']:
                hours_df = pd.DataFrame(
                    list(st.session_state.message_stats['hourly_activity'].items()),
                    columns=['Hour', 'Messages']
                )
                hours_df = hours_df.sort_values('Hour')
                fig_hourly = px.line(hours_df, x='Hour', y='Messages',
                                    title="Activity by Hour",
                                    markers=True)
                fig_hourly.update_layout(height=300)
                st.plotly_chart(fig_hourly, use_container_width=True)
        
        # Word cloud simulation (top words)
        st.subheader("🔤 Most Used Words")
        if st.session_state.message_stats['word_frequency']:
            top_words = sorted(st.session_state.message_stats['word_frequency'].items(), 
                             key=lambda x: x[1], reverse=True)[:10]
            words_df = pd.DataFrame(top_words, columns=['Word', 'Frequency'])
            
            fig_words = px.bar(words_df, x='Frequency', y='Word', 
                              orientation='h', title="Top 10 Words",
                              color='Frequency', color_continuous_scale='blues')
            fig_words.update_layout(height=400)
            st.plotly_chart(fig_words, use_container_width=True)
        
        # Chat timeline
        st.subheader("📅 Conversation Timeline")
        if len(st.session_state.messages) > 1:
            timeline_data = []
            for msg in st.session_state.messages:
                if 'timestamp' in msg:
                    timeline_data.append({
                        'Time': msg['timestamp'][:19],
                        'Speaker': 'You' if msg['role'] == 'user' else 'Bot',
                        'Message Length': len(msg['content']),
                        'Sentiment': msg.get('sentiment', 'neutral')
                    })
            
            if timeline_data:
                timeline_df = pd.DataFrame(timeline_data)
                fig_timeline = px.scatter(timeline_df, x='Time', y='Message Length',
                                        color='Speaker', size='Message Length',
                                        hover_data=['Sentiment'],
                                        title="Message Timeline")
                fig_timeline.update_layout(height=300)
                st.plotly_chart(fig_timeline, use_container_width=True)
    else:
        st.info("Start chatting to see analytics! The more you chat, the more interesting the data becomes! 📊")

with tab3:
    st.header("⚙️ Settings & Preferences")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Chat Preferences")
        
        # Chat style selector
        chat_style = st.selectbox(
            "Bot Personality",
            ["Friendly", "Professional", "Funny", "Philosophical"],
            index=0
        )
        
        # Emoji usage
        use_emojis = st.checkbox("Use emojis in responses", value=True)
        
        # Response speed simulation
        response_speed = st.slider("Response speed (ms)", 0, 2000, 500)
        
        if st.button("Save Preferences"):
            st.session_state.user_preferences['chat_style'] = chat_style.lower()
            st.session_state.user_preferences['emoji_usage'] = use_emojis
            st.success("Preferences saved! ✅")
    
    with col2:
        st.subheader("Data Management")
        
        # Export chat data
        if st.button("📥 Export Chat History"):
            chat_data = {
                'messages': st.session_state.messages,
                'stats': st.session_state.message_stats,
                'exported_at': datetime.now().isoformat()
            }
            json_str = json.dumps(chat_data, indent=2)
            st.download_button(
                label="Download JSON",
                data=json_str,
                file_name=f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )
        
        # Clear data
        if st.button("🗑️ Clear All Data", type="secondary"):
            st.session_state.messages = []
            st.session_state.message_stats = {
                'total_messages': 0,
                'user_messages': 0,
                'bot_messages': 0,
                'topics': {},
                'hourly_activity': {},
                'word_frequency': {},
                'response_times': [],
                'sentiment_scores': {'positive': 0, 'neutral': 0, 'negative': 0}
            }
            st.success("All data cleared!")
            st.rerun()

# Footer
st.markdown("---")
st.success("""
**🎯 Day 3 Challenge**: Can you add these analytics features?
- Track response time between messages
- Create a "mood over time" chart
- Add a word count comparison
- Build a conversation quality score
""")

"""
🚀 Tomorrow: We'll save all this data to a real database so it persists between sessions!
"""