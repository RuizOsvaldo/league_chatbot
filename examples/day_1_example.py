"""
Day 1 Example: Your First Chatbot!
The LEAGUE of Amazing Programmers

Learn the basics of Streamlit by building a simple chat interface.
Run: streamlit run day_1_example.py
"""

import streamlit as st
from datetime import datetime
import pytz

# Page setup - this makes your app look good!
st.set_page_config(
    page_title="My First Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Main title
st.title("🤖 My First Chatbot")
st.write("Welcome to Day 1! Let's build a basic chat interface.")

# Section 1: Understanding Streamlit Basics
st.header("📚 What We're Learning")

st.info("""
**Today's Goals:**
- ✅ Create a chat interface using Streamlit
- ✅ Display messages
- ✅ Get user input
- ✅ Make the bot respond
- ✅ Add some personality!
""")

# Section 2: Simple Chat Display
st.header("💬 Let's Chat!")

# This is how we store chat history - session state is like the app's memory
if 'messages' not in st.session_state:
    st.session_state.messages = []
    # Add a welcome message
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Hey! I'm your first chatbot! 👋 Try saying hello!"
    })

# Display all messages in the chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Section 3: Getting User Input
# This creates the chat input box at the bottom
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Simple bot response logic
    bot_response = ""
    
    # Check what the user said and respond accordingly
    if "hello" in prompt.lower() or "hi" in prompt.lower():
        bot_response = "Hey there! 😊 How's it going?"
    elif "how are you" in prompt.lower():
        bot_response = "I'm doing great! I'm a brand new chatbot and excited to chat!"
    elif "name" in prompt.lower():
        bot_response = "I don't have a name yet! What would you like to call me?"
    elif "bye" in prompt.lower() or "goodbye" in prompt.lower():
        bot_response = "See you later! Thanks for chatting! 👋"
    elif "?" in prompt:
        bot_response = "That's a great question! I'm still learning, but I'll try my best!"
    else:
        # Default response for everything else
        responses = [
            "That's interesting! Tell me more!",
            "Cool! I hadn't thought about that.",
            "Wow, really? That's awesome!",
            "I see what you mean!",
            "That makes sense!"
        ]
        # Pick a response based on message length (just for variety)
        import random
        bot_response = random.choice(responses)
    
    # Add bot response to chat
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    
    # Refresh the page to show new messages
    st.rerun()

# Section 4: Fun Stats Sidebar
st.sidebar.header("📊 Chat Stats")
st.sidebar.metric("Total Messages", len(st.session_state.messages))

# Count user vs bot messages
user_messages = sum(1 for m in st.session_state.messages if m["role"] == "user")
bot_messages = sum(1 for m in st.session_state.messages if m["role"] == "assistant")

st.sidebar.metric("Your Messages", user_messages)
st.sidebar.metric("Bot Messages", bot_messages)

# Add current time
st.sidebar.markdown("---")
pst_tz = pytz.timezone('US/Pacific')
pst_time = datetime.now(pst_tz)
current_time_pst = pst_time.strftime("%I:%M %p PST")
st.sidebar.write(f"🕐 Current Time: {current_time_pst}")

# Section 5: Learning Tips
with st.expander("💡 How This Works"):
    st.markdown("""
    **Key Concepts:**
    
    1. **Session State**: Stores data between interactions
    ```python
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    ```
    
    2. **Chat Message**: Creates chat bubbles
    ```python
    with st.chat_message("user"):
        st.write("Hello!")
    ```
    
    3. **Chat Input**: Gets user text
    ```python
    if prompt := st.chat_input():
        # Do something with prompt
    ```
    
    4. **Rerun**: Refreshes the page
    ```python
    st.rerun()
    ```
    """)

# Clear chat button
if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Chat cleared! Let's start fresh! 👋"
    })
    st.rerun()

# Footer
st.markdown("---")
st.caption("🎉 Congrats! You've built your first chatbot! Tomorrow we'll add more personality!")

# Fun challenge box
st.success("""
**🎯 Day 1 Challenge**: Can you add these features?
- Make the bot respond to "joke" with a funny joke
- Add a response for when someone asks about the weather
- Create a special response for your name
""")

"""
💭 Think About It:
- What kind of personality do you want your bot to have?
- What special features would make it unique?
- Who would use your chatbot and why?

Tomorrow we'll make your bot even smarter! 🚀
"""