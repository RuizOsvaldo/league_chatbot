"""
Day 3 Template: Add Analytics & Beautiful Visualizations
The LEAGUE of Amazing Programmers

Track conversations, visualize patterns, and make your chatbot data-driven!
Run: streamlit run day_3.py
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import random

# TODO 1: Set up page with wide layout for charts
# Use st.set_page_config() with:
# - page_title="Analytics Chatbot"
# - page_icon="📊"
# - layout="wide" (for better chart display)
# YOUR CODE HERE:


# TODO 2: Create title with description
# Explain that this bot tracks and analyzes conversations
# YOUR CODE HERE:


# TODO 3: Initialize comprehensive session state
# You'll need:
# - messages (with timestamps and metadata)
# - message_stats (dictionary with various counters)
# - user_preferences
# - chat_analytics
# YOUR CODE HERE:
if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'message_stats' not in st.session_state:
    st.session_state.message_stats = {
        'total_messages': 0,
        'user_messages': 0,
        'bot_messages': 0,
        'topics': {},
        'word_frequency': {},
        'sentiment_scores': {},
        'hourly_activity': {}
    }


# TODO 4: Create sentiment analysis function
def analyze_sentiment(text):
    """Analyze the sentiment of text (positive, neutral, negative)"""
    # TODO: Implement simple sentiment analysis
    # Check for positive words (good, great, love, excellent, etc.)
    # Check for negative words (bad, hate, terrible, awful, etc.)
    # Return 'positive', 'neutral', or 'negative'
    # YOUR CODE HERE:
    
    return 'neutral'  # Default return


# TODO 5: Create topic detection function
def detect_topic(text):
    """Detect the topic of conversation"""
    # TODO: Implement topic detection
    # Categories: tech, school, gaming, music, sports, food, general
    # Check for keywords in each category
    # Return the detected topic
    # YOUR CODE HERE:
    
    return 'general'  # Default return


# TODO 6: Create statistics update function
def update_statistics(message, role):
    """Update all statistics when a new message is added"""
    # TODO: Update various statistics:
    # - Message counts (total, user, bot)
    # - Topic frequency
    # - Word frequency (words > 3 characters)
    # - Sentiment tracking
    # - Hourly activity (what hour messages are sent)
    # YOUR CODE HERE:
    pass


# TODO 7: Create main layout with tabs
# Create tabs for: Chat, Analytics, Settings
# Use st.tabs()
# YOUR CODE HERE:


# TODO 8: Implement Chat tab
# In the Chat tab:
# - Display messages with timestamps
# - Show quick stats in a sidebar or column
# - Add chat input with enhanced processing
# YOUR CODE HERE:


# TODO 9: Create response function with analytics
def get_analytics_aware_response(user_input):
    """Generate responses that reference analytics"""
    # TODO: Create responses that mention:
    # - User's chat patterns
    # - Detected sentiment
    # - Topic of conversation
    # - Interesting statistics
    # YOUR CODE HERE:
    
    return "Let's track this conversation!"


# TODO 10: Implement Analytics tab
# In the Analytics tab, create:


# TODO 11: Message distribution pie chart
# Show ratio of user vs bot messages
# Use plotly.graph_objects.Pie
# YOUR CODE HERE:


# TODO 12: Topics bar chart
# Show frequency of different topics
# Use plotly.express.bar
# YOUR CODE HERE:


# TODO 13: Sentiment analysis chart
# Show positive/neutral/negative distribution
# Use colors: green for positive, yellow for neutral, red for negative
# YOUR CODE HERE:


# TODO 14: Activity timeline
# Show when messages are sent (by hour)
# Use plotly.express.line or bar
# YOUR CODE HERE:


# TODO 15: Word cloud (or top words bar chart)
# Show most frequently used words
# Filter out common words (the, is, are, etc.)
# YOUR CODE HERE:


# TODO 16: Conversation flow visualization
# Show message length over time
# Or response time between messages
# YOUR CODE HERE:


# TODO 17: Create metrics cards
# Display key metrics in columns:
# - Average message length
# - Most active hour
# - Dominant sentiment
# - Favorite topic
# Use st.metric() for nice display
# YOUR CODE HERE:


# TODO 18: Implement Settings tab
# In the Settings tab, add:
# - Toggle for showing timestamps
# - Choose chart colors/themes
# - Set analysis preferences
# - Export options
# YOUR CODE HERE:


# TODO 19: Add data export functionality
# Create export options for:
# - Chat history (CSV)
# - Analytics report (JSON)
# - Charts (PNG images)
# Use st.download_button()
# YOUR CODE HERE:


# TODO 20: Create conversation insights
# Generate automatic insights like:
# - "You're most active at 3 PM"
# - "Your conversations are 80% positive!"
# - "You love talking about gaming"
# Display as info boxes
# YOUR CODE HERE:


# TODO 21: Add comparison features
# Compare:
# - Today vs yesterday
# - This week vs last week
# - Morning vs evening conversations
# YOUR CODE HERE:


# TODO 22: Create achievement badges
# Award badges for:
# - 100 messages milestone
# - Positive conversation streak
# - Topic variety
# - Daily chat streak
# Display visually with emojis/icons
# YOUR CODE HERE:


# TODO 23: Add real-time updates
# Update charts automatically as new messages come in
# Show live statistics
# Add refresh button for manual updates
# YOUR CODE HERE:


# TODO 24: Create a conversation quality score
# Calculate based on:
# - Message length variety
# - Topic diversity
# - Sentiment balance
# - Engagement level
# Display as a gauge or progress bar
# YOUR CODE HERE:


# TODO 25: Polish the analytics experience
# Add:
# - Smooth animations for charts
# - Helpful tooltips
# - Color coordination
# - Mobile-responsive design
# YOUR CODE HERE:


"""
🎯 Challenges when complete:
1. Add prediction: "Based on patterns, you'll send 50 messages today"
2. Create a mood tracker that changes chart colors
3. Add conversation goals (e.g., "Stay positive for 10 messages")
4. Create a weekly report that emails/downloads automatically
5. Add conversation recommendations based on analytics

💡 Advanced Analytics Ideas:
- Emotion wheel visualization
- Network graph of topic connections
- Heatmap of activity by day/hour
- Sentiment trend predictor
- Conversation health score

When complete, your chatbot should:
✅ Track all conversation metrics
✅ Display beautiful interactive charts
✅ Provide conversation insights
✅ Export data in multiple formats
✅ Show real-time statistics
✅ Detect topics and sentiment
✅ Award achievement badges
✅ Generate automatic reports
"""