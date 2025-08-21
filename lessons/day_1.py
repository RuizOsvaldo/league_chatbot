"""
Day 1 Template: Build Your First Chatbot!
The LEAGUE of Amazing Programmers

Complete the TODOs to create your own chatbot with basic chat functionality.
Run: streamlit run day_1.py
"""

import streamlit as st
from datetime import datetime

# TODO 1: Set up the page configuration
# Use st.set_page_config() with:
# - page_title="My Chatbot"
# - page_icon="🤖" (or choose your own emoji!)
# - layout="centered"
# YOUR CODE HERE:


# TODO 2: Create a title for your chatbot
# Give your chatbot a cool name!
# Use st.title() to display it
# YOUR CODE HERE:


# TODO 3: Add a welcome message
# Use st.write() to explain what your chatbot does
# YOUR CODE HERE:


# TODO 4: Initialize session state for messages
# Session state is like your app's memory
# Check if 'messages' exists in st.session_state
# If not, create it as an empty list
# Hint: if 'messages' not in st.session_state:
#          st.session_state.messages = []
# YOUR CODE HERE:


# TODO 5: Add a welcome message from your bot
# If the messages list is empty, add a welcome message
# The message should be a dictionary with "role" and "content"
# Example: {"role": "assistant", "content": "Hello! I'm your chatbot!"}
# YOUR CODE HERE:


# TODO 6: Display all messages in the chat
# Loop through st.session_state.messages
# Use st.chat_message() to display each message
# Inside the chat_message, use st.write() to show the content
# YOUR CODE HERE:


# TODO 7: Create the chat input
# Use st.chat_input() to get user input
# Store it in a variable (like 'prompt')
# Hint: if prompt := st.chat_input("Your message..."):
# YOUR CODE HERE:


# TODO 8: Process user input
# Inside the if statement from TODO 7:
# - Add the user's message to st.session_state.messages
# - Create a simple bot response
# - Add the bot's response to st.session_state.messages
# - Use st.rerun() to refresh the page
# YOUR CODE HERE:


# TODO 9: Create simple bot responses
# Make your bot respond to different inputs
# Check for keywords like "hello", "how are you", "bye"
# Return different responses based on the input
# YOUR CODE HERE:
def get_bot_response(user_input):
    """Generate a response based on user input"""
    # Convert input to lowercase for easier matching
    user_input_lower = user_input.lower()
    
    # TODO: Add your response logic here
    # Example:
    # if "hello" in user_input_lower:
    #     return "Hi there! How can I help you?"
    
    # Default response
    return "That's interesting! Tell me more!"


# TODO 10: Add a sidebar with information
# Use st.sidebar to add:
# - A header showing "Chat Info"
# - Display the total number of messages
# - Show the current time
# - Add a clear chat button
# YOUR CODE HERE:


# TODO 11: Add a clear chat button functionality
# If the clear button is clicked:
# - Clear the messages list
# - Add a new welcome message
# - Use st.rerun() to refresh
# YOUR CODE HERE:


# TODO 12: Make it more interactive
# Add at least 3 different responses for your bot
# Ideas:
# - Respond to "joke" with a joke
# - Respond to "time" with the current time
# - Respond to "help" with available commands
# YOUR CODE HERE:


# TODO 13: Add some personality
# Give your bot a unique personality by:
# - Using emojis in responses
# - Adding random responses for variety
# - Creating a consistent tone (friendly, funny, professional)
# YOUR CODE HERE:


# TODO 14: Display chat statistics
# Show interesting stats like:
# - Number of user messages vs bot messages
# - Average message length
# - Most used words
# YOUR CODE HERE:


# TODO 15: Add a fun feature
# Choose one:
# - Add a "thinking" animation when the bot responds
# - Use different chat bubble colors
# - Add sound effects (using st.audio)
# - Show the bot's "mood" based on conversation
# YOUR CODE HERE:


"""
🎯 Challenges when you're done:
1. Make the bot respond to your name
2. Add 5 different joke responses
3. Create a help menu that lists all commands
4. Add emoji reactions to messages
5. Make the bot remember information from the conversation

💡 Tips:
- Test your chatbot after each TODO
- Try talking to it like a real person
- Ask friends to test it and give feedback
- Keep responses friendly and helpful
- Have fun with it!

When complete, your chatbot should:
✅ Display messages in chat bubbles
✅ Respond to user input
✅ Have multiple response patterns
✅ Show chat statistics
✅ Have a clear chat function
✅ Feel interactive and fun to use
"""