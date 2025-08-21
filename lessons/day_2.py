"""
Day 2 Template: Make Your Chatbot Smart!
The LEAGUE of Amazing Programmers

Add personality, moods, and intelligence to your chatbot.
Run: streamlit run day_2.py
"""

import streamlit as st
import random
from datetime import datetime

# TODO 1: Set up the page with style
# Use st.set_page_config() with:
# - page_title="Smart Chatbot"
# - page_icon="🧠" (or your choice)
# - layout="centered"
# YOUR CODE HERE:


# TODO 2: Create title and description
# Make it clear this is an upgraded version!
# YOUR CODE HERE:


# TODO 3: Initialize session state variables
# You'll need:
# - messages (list)
# - bot_mood (string, default "happy")
# - user_name (string or None)
# - conversation_stats (dictionary)
# YOUR CODE HERE:


# TODO 4: Define bot moods/personalities
# Create a dictionary with at least 3 moods
# Each mood should have:
# - emoji
# - description
# - response style
# Example:
# MOODS = {
#     "happy": {"emoji": "😊", "style": "cheerful"},
#     "sleepy": {"emoji": "😴", "style": "tired"}
# }
# YOUR CODE HERE:


# TODO 5: Create joke collection
# Make a list of at least 5 jokes
# YOUR CODE HERE:
JOKES = [
    # Add your jokes here
]


# TODO 6: Create fun facts collection
# Make a list of at least 5 interesting facts
# YOUR CODE HERE:
FUN_FACTS = [
    # Add your facts here
]


# TODO 7: Build intelligent response system
def get_smart_response(user_input):
    """Generate intelligent responses based on input and mood"""
    user_input_lower = user_input.lower()
    
    # TODO 8: Check if user is introducing themselves
    # Look for "my name is" or "i am" or "i'm"
    # Save their name to session state
    # Respond with personalized greeting
    # YOUR CODE HERE:
    
    
    # TODO 9: Add mood detection and responses
    # Check if user asks about bot's mood
    # Respond based on current mood
    # YOUR CODE HERE:
    
    
    # TODO 10: Add mood changing commands
    # Let users change the bot's mood
    # Example: "be happy", "be silly"
    # Update st.session_state.bot_mood
    # YOUR CODE HERE:
    
    
    # TODO 11: Add joke functionality
    # If user asks for a joke
    # Return a random joke from your collection
    # Keep track of jokes told
    # YOUR CODE HERE:
    
    
    # TODO 12: Add fun fact functionality
    # If user asks for a fact
    # Return a random fact
    # YOUR CODE HERE:
    
    
    # TODO 13: Add math capability
    # Detect math expressions (containing +, -, *, /)
    # Calculate and return the result
    # Handle errors gracefully
    # YOUR CODE HERE:
    
    
    # TODO 14: Add time/date responses
    # If user asks for time or date
    # Return current time/date
    # YOUR CODE HERE:
    
    
    # TODO 15: Add game suggestion for boredom
    # If user says they're bored
    # Suggest a game or activity
    # YOUR CODE HERE:
    
    
    # TODO 16: Create mood-based default responses
    # Different response styles for each mood
    # Use the current bot mood to select style
    # YOUR CODE HERE:
    
    
    return "I'm still learning! Can you teach me?"


# TODO 17: Create sidebar with bot controls
# Add:
# - Current mood display
# - Mood selector (selectbox or buttons)
# - Statistics (jokes told, facts shared, etc.)
# - User name display (if known)
# YOUR CODE HERE:


# TODO 18: Implement chat display
# Show all messages with chat_message
# Add timestamps to messages (optional)
# YOUR CODE HERE:


# TODO 19: Implement chat input handling
# Get user input
# Process it with get_smart_response()
# Add both messages to session state
# Rerun the app
# YOUR CODE HERE:


# TODO 20: Add special features
# Choose at least 2:
# - Typing indicator (show "Bot is typing...")
# - Message reactions (thumbs up/down)
# - Voice input simulation
# - Export chat history
# - Message search
# YOUR CODE HERE:


# TODO 21: Create a mini-game
# Add one simple game:
# - 20 questions
# - Word association
# - Riddles
# - Trivia
# YOUR CODE HERE:


# TODO 22: Add memory feature
# Make the bot remember things:
# - User's favorite color
# - Previous topics discussed
# - User preferences
# Store in session state
# YOUR CODE HERE:


# TODO 23: Create help system
# Add a help command that shows:
# - Available commands
# - How to change moods
# - Available games
# - Special features
# YOUR CODE HERE:


# TODO 24: Add achievement system
# Track milestones like:
# - First joke told
# - 10 messages sent
# - All moods unlocked
# - Game won
# Show achievements in sidebar
# YOUR CODE HERE:


# TODO 25: Polish the experience
# Add:
# - Welcome back message for returning users
# - Smooth transitions between moods
# - Error handling for all features
# - Loading states where appropriate
# YOUR CODE HERE:


"""
🎯 Challenges when complete:
1. Add 5 different bot moods with unique personalities
2. Create a mood that changes based on conversation
3. Add a secret command that unlocks a special feature
4. Make the bot learn new responses from the user
5. Create a conversation quality score

💡 Advanced Features to Try:
- Sentiment analysis (positive/negative detection)
- Multi-language greetings
- Bot avatar that changes with mood
- Conversation topics tracker
- Daily challenges or questions

When complete, your chatbot should:
✅ Have multiple personalities/moods
✅ Remember the user's name
✅ Tell jokes and facts
✅ Solve math problems
✅ Play simple games
✅ Respond intelligently to various inputs
✅ Show personality in responses
✅ Track conversation statistics
"""