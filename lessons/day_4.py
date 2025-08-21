"""
Day 4 Template: Add Database Memory to Your Chatbot
The LEAGUE of Amazing Programmers

Save conversations permanently with SQLite database!
Run: streamlit run day_4.py
"""

import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime
import json

# TODO 1: Set up page configuration
# Use st.set_page_config() with:
# - page_title="Database Chatbot"
# - page_icon="💾"
# - layout="wide"
# YOUR CODE HERE:


# TODO 2: Create title and description
# Explain that the bot now has permanent memory
# YOUR CODE HERE:


# TODO 3: Create database initialization function
def init_database():
    """Initialize the SQLite database with necessary tables"""
    # TODO 4: Connect to database
    # Use sqlite3.connect('chatbot.db')
    # YOUR CODE HERE:
    
    # TODO 5: Create messages table
    # Columns needed:
    # - id (INTEGER PRIMARY KEY AUTOINCREMENT)
    # - session_id (TEXT)
    # - username (TEXT)
    # - role (TEXT)
    # - content (TEXT)
    # - timestamp (DATETIME DEFAULT CURRENT_TIMESTAMP)
    # - sentiment (TEXT)
    # YOUR CODE HERE:
    
    # TODO 6: Create users table
    # Columns needed:
    # - id (INTEGER PRIMARY KEY AUTOINCREMENT)
    # - username (TEXT UNIQUE)
    # - created_at (DATETIME DEFAULT CURRENT_TIMESTAMP)
    # - last_seen (DATETIME)
    # - total_messages (INTEGER DEFAULT 0)
    # - preferences (TEXT)
    # YOUR CODE HERE:
    
    # TODO 7: Create custom_responses table
    # For teaching the bot new responses
    # Columns needed:
    # - id (INTEGER PRIMARY KEY AUTOINCREMENT)
    # - trigger (TEXT)
    # - response (TEXT)
    # - created_by (TEXT)
    # - usage_count (INTEGER DEFAULT 0)
    # YOUR CODE HERE:
    
    pass


# TODO 8: Initialize database when app starts
# Call init_database()
# YOUR CODE HERE:


# TODO 9: Create function to save messages
def save_message(session_id, username, role, content, sentiment=None):
    """Save a message to the database"""
    # TODO: Implement message saving
    # - Connect to database
    # - Insert message
    # - Commit and close
    # YOUR CODE HERE:
    pass


# TODO 10: Create function to load conversation history
def load_conversation_history(username=None, limit=50):
    """Load conversation history from database"""
    # TODO: Implement history loading
    # - Connect to database
    # - Query messages (filter by username if provided)
    # - Return as pandas DataFrame
    # - Close connection
    # YOUR CODE HERE:
    return pd.DataFrame()  # Replace with actual data


# TODO 11: Create function to get/create user
def get_or_create_user(username):
    """Get existing user or create new one"""
    # TODO: Implement user management
    # - Check if user exists
    # - If not, create new user
    # - Update last_seen
    # - Return user info
    # YOUR CODE HERE:
    pass


# TODO 12: Create function to update user stats
def update_user_stats(username):
    """Update user statistics"""
    # TODO: Implement stats update
    # - Increment message count
    # - Update last_seen
    # - Other statistics
    # YOUR CODE HERE:
    pass


# TODO 13: Create function to add custom response
def add_custom_response(trigger, response, created_by):
    """Add a custom bot response to database"""
    # TODO: Implement custom response saving
    # - Insert into custom_responses table
    # - Handle duplicates
    # YOUR CODE HERE:
    pass


# TODO 14: Create function to get custom response
def get_custom_response(user_input):
    """Check for custom responses matching input"""
    # TODO: Implement custom response retrieval
    # - Search for matching triggers
    # - Update usage count if found
    # - Return response or None
    # YOUR CODE HERE:
    return None


# TODO 15: Create function to search messages
def search_messages(search_term, username=None):
    """Search through message history"""
    # TODO: Implement message search
    # - Use SQL LIKE for searching
    # - Filter by username if provided
    # - Return matching messages
    # YOUR CODE HERE:
    return pd.DataFrame()


# TODO 16: Initialize session state
# Add:
# - session_id (unique for each session)
# - current_user (username)
# - messages (for current session)
# YOUR CODE HERE:


# TODO 17: Create user login/registration sidebar
# In st.sidebar:
# - Text input for username
# - Login/Register button
# - Show user stats if logged in
# - Logout button
# YOUR CODE HERE:


# TODO 18: Create main interface with tabs
# Tabs needed:
# - Chat
# - History
# - Teach Bot
# - Search
# YOUR CODE HERE:


# TODO 19: Implement Chat tab
# In Chat tab:
# - Check if user is logged in
# - Display messages
# - Handle input
# - Save messages to database
# - Check for custom responses first
# YOUR CODE HERE:


# TODO 20: Implement History tab
# In History tab:
# - Load conversation history
# - Display in a nice table/format
# - Add filters (date range, session)
# - Export option
# YOUR CODE HERE:


# TODO 21: Implement Teach Bot tab
# In Teach Bot tab:
# - Form to add custom responses
# - Input for trigger phrase
# - Input for response
# - Submit button
# - Show existing custom responses
# YOUR CODE HERE:


# TODO 22: Implement Search tab
# In Search tab:
# - Search input field
# - Search button
# - Display results
# - Highlight search terms
# YOUR CODE HERE:


# TODO 23: Create database statistics display
# Show:
# - Total messages in database
# - Total users
# - Most active user
# - Custom responses count
# Display in sidebar or separate section
# YOUR CODE HERE:


# TODO 24: Add data backup/export functionality
# Create options to:
# - Export all user data
# - Backup database
# - Clear old messages
# - Download conversation as PDF/TXT
# YOUR CODE HERE:


# TODO 25: Add advanced database features
# Choose at least 2:
# - Message reactions (like/dislike)
# - Conversation threads
# - Message editing history
# - User blocking/privacy
# - Scheduled messages
# YOUR CODE HERE:


"""
🎯 Challenges when complete:
1. Add conversation topics/tags for organization
2. Create a favorites system for messages
3. Add user profiles with avatars
4. Implement message encryption for privacy
5. Create database migration system for updates

💡 Database Best Practices:
- Always close connections
- Use parameterized queries (?, ?) to prevent SQL injection
- Create indexes for frequently searched columns
- Backup database regularly
- Handle connection errors gracefully

When complete, your chatbot should:
✅ Save all conversations permanently
✅ Remember users between sessions
✅ Learn custom responses
✅ Search through history
✅ Export conversation data
✅ Show user statistics
✅ Handle multiple users
✅ Persist data even after app restart
"""