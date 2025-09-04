"""
Day 3 Example: API-Powered Chatbot
The LEAGUE of Amazing Programmers

Connect your chatbot to real-world data and services!
Run: streamlit run day_3_example.py
"""

import streamlit as st
import requests
import json
import random
from datetime import datetime
import time

# Page setup
st.set_page_config(
    page_title="API-Powered Chatbot",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 Day 3: API-Powered Chatbot")
st.write("Your bot is now connected to the real world! Ask about weather, jokes, facts, and more!")

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "🌐 Hey! I'm now connected to the internet! I can get real weather, fresh jokes, interesting facts, and more! Try asking: 'What's the weather?' or 'Tell me a joke!' 🚀"
    })

if 'api_usage_stats' not in st.session_state:
    st.session_state.api_usage_stats = {
        'weather_calls': 0,
        'jokes_fetched': 0,
        'facts_retrieved': 0,
        'quotes_shared': 0,
        'total_api_calls': 0
    }

if 'user_location' not in st.session_state:
    st.session_state.user_location = "New York"

# API Functions
def get_weather_data(city="New York"):
    """Get weather using a free weather API"""
    try:
        # Using OpenWeatherMap API (you'd need an API key for real implementation)
        # For demo purposes, we'll simulate the response
        
        # Simulate API call delay
        time.sleep(0.5)
        
        # Mock weather data
        weather_conditions = ["sunny", "cloudy", "rainy", "partly cloudy", "clear"]
        temperatures = [65, 72, 68, 75, 70, 78, 62]
        
        temp = random.choice(temperatures)
        condition = random.choice(weather_conditions)
        
        # Simulate occasional API failures
        if random.random() < 0.1:  # 10% chance of "failure"
            raise requests.exceptions.ConnectionError("Weather service temporarily unavailable")
        
        st.session_state.api_usage_stats['weather_calls'] += 1
        st.session_state.api_usage_stats['total_api_calls'] += 1
        
        return f"🌤️ It's {temp}°F and {condition} in {city}! Perfect weather for coding! 😎"
        
    except Exception as e:
        return f"😔 Couldn't get weather data right now: {str(e)}"

def get_random_joke():
    """Fetch a joke from joke API"""
    try:
        # In real implementation, you'd call:
        # response = requests.get("https://official-joke-api.appspot.com/random_joke")
        # joke_data = response.json()
        
        jokes = [
            {"setup": "Why don't scientists trust atoms?", "punchline": "Because they make up everything! 🤣"},
            {"setup": "What do you call a fake noodle?", "punchline": "An impasta! 🍝"},
            {"setup": "Why did the scarecrow win an award?", "punchline": "He was outstanding in his field! 🌾"},
            {"setup": "What do you call a bear with no teeth?", "punchline": "A gummy bear! 🐻"},
            {"setup": "Why don't eggs tell jokes?", "punchline": "They'd crack each other up! 🥚"},
            {"setup": "What did the ocean say to the beach?", "punchline": "Nothing, it just waved! 🌊"},
            {"setup": "Why did the math book look so sad?", "punchline": "Because it had too many problems! 📚"}
        ]
        
        joke = random.choice(jokes)
        
        st.session_state.api_usage_stats['jokes_fetched'] += 1
        st.session_state.api_usage_stats['total_api_calls'] += 1
        
        return f"😄 {joke['setup']}\n\n{joke['punchline']}"
        
    except Exception as e:
        return f"😅 Joke API is having a bad day: {str(e)}"

def get_random_fact():
    """Get an interesting fact"""
    try:
        facts = [
            "🐙 Octopuses have three hearts and blue blood!",
            "🍯 Honey never spoils - archaeologists have found 3000-year-old honey that's still edible!",
            "🦒 A giraffe's tongue is about 20 inches long and is blue-black in color!",
            "⚡ Lightning strikes the Earth about 100 times per second!",
            "🌙 Footprints on the moon will last millions of years because there's no wind!",
            "🧠 Your brain uses about 20% of your body's total energy!",
            "🐧 Penguins have knees - they're just hidden inside their bodies!",
            "🍕 Pizza was originally considered peasant food in Italy!",
            "🦈 Sharks have been around longer than trees!",
            "🌍 If you could fold a piece of paper 42 times, it would reach the moon!"
        ]
        
        fact = random.choice(facts)
        
        st.session_state.api_usage_stats['facts_retrieved'] += 1
        st.session_state.api_usage_stats['total_api_calls'] += 1
        
        return f"🤓 Here's a cool fact: {fact}"
        
    except Exception as e:
        return f"🤔 Facts API is taking a break: {str(e)}"

def get_inspirational_quote():
    """Get a motivational quote"""
    try:
        quotes = [
            {"text": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
            {"text": "Innovation distinguishes between a leader and a follower.", "author": "Steve Jobs"},
            {"text": "Code is like humor. When you have to explain it, it's bad.", "author": "Cory House"},
            {"text": "First, solve the problem. Then, write the code.", "author": "John Johnson"},
            {"text": "Programming isn't about what you know; it's about what you can figure out.", "author": "Chris Pine"},
            {"text": "The best error message is the one that never shows up.", "author": "Thomas Fuchs"},
            {"text": "Simplicity is the ultimate sophistication.", "author": "Leonardo da Vinci"},
            {"text": "Any fool can write code that a computer can understand. Good programmers write code that humans can understand.", "author": "Martin Fowler"}
        ]
        
        quote = random.choice(quotes)
        
        st.session_state.api_usage_stats['quotes_shared'] += 1
        st.session_state.api_usage_stats['total_api_calls'] += 1
        
        return f"💭 \"{quote['text']}\"\n\n— {quote['author']}"
        
    except Exception as e:
        return f"💔 Quote API is feeling uninspired: {str(e)}"

def get_programming_tip():
    """Get a programming tip"""
    tips = [
        "💡 Always write comments explaining WHY you did something, not just what you did!",
        "🔧 Use meaningful variable names - 'user_age' is better than 'x'!",
        "🧪 Test your code with weird inputs - what happens if someone types 'banana' instead of a number?",
        "📁 Keep your functions short and focused - one function should do one thing well!",
        "🔍 When debugging, explain your code to a rubber duck (or friend) - you'll often find the bug!",
        "💾 Save your work frequently - nothing hurts more than losing hours of coding!",
        "📚 Read other people's code - it's like learning new vocabulary!",
        "🎯 Start with the simplest version that works, then improve it!",
        "🤝 Don't be afraid to ask for help - every programmer googles things constantly!",
        "⏰ Take breaks! Your brain solves problems better when it's rested!"
    ]
    
    return random.choice(tips)

def handle_api_request(user_input):
    """Determine which API to call based on user input"""
    user_input_lower = user_input.lower()
    
    # Weather requests
    if any(word in user_input_lower for word in ['weather', 'temperature', 'forecast', 'rain', 'sunny', 'cloudy']):
        # Try to extract city name
        city = st.session_state.user_location
        if " in " in user_input_lower:
            try:
                city = user_input_lower.split(" in ")[1].split()[0].title()
            except:
                pass
        return get_weather_data(city)
    
    # Joke requests
    elif any(word in user_input_lower for word in ['joke', 'funny', 'laugh', 'humor', 'make me laugh']):
        return get_random_joke()
    
    # Fact requests
    elif any(word in user_input_lower for word in ['fact', 'interesting', 'learn', 'trivia', 'teach me']):
        return get_random_fact()
    
    # Quote requests
    elif any(word in user_input_lower for word in ['quote', 'inspiration', 'motivate', 'inspire']):
        return get_inspirational_quote()
    
    # Programming tips
    elif any(word in user_input_lower for word in ['coding tip', 'programming tip', 'advice', 'help me code']):
        return get_programming_tip()
    
    return None  # No API match found

def get_smart_response(user_input):
    """Generate intelligent responses with API integration"""
    # First, try to handle with APIs
    api_response = handle_api_request(user_input)
    if api_response:
        return api_response
    
    # Regular responses
    user_input_lower = user_input.lower()
    
    if any(word in user_input_lower for word in ['hello', 'hi', 'hey', 'sup']):
        return "Hey there! 🌐 I'm your internet-connected chatbot! Try asking me about the weather, for a joke, some facts, or inspiration!"
    
    elif 'help' in user_input_lower or 'what can you do' in user_input_lower:
        return """🌐 **I'm connected to the real world!** Here's what I can do:

🌤️ **Weather**: "What's the weather?" or "Weather in Tokyo"
😄 **Jokes**: "Tell me a joke" or "Make me laugh"  
🧠 **Facts**: "Give me a fact" or "Teach me something"
💭 **Quotes**: "Inspire me" or "Give me a quote"
💻 **Coding Tips**: "Give me a coding tip"

Just ask naturally - I'll understand! 🚀"""
    
    elif any(word in user_input_lower for word in ['thanks', 'thank you']):
        return "You're welcome! 😊 Want to try another API feature? I love showing off my internet connection! 🌐"
    
    elif any(word in user_input_lower for word in ['bye', 'goodbye', 'see you']):
        api_count = st.session_state.api_usage_stats['total_api_calls']
        return f"Goodbye! 👋 We made {api_count} API calls together today! Thanks for testing my internet powers! 🌐"
    
    else:
        suggestions = [
            "🤔 I'm not sure about that, but I can get you the weather! Try 'What's the weather?'",
            "🎭 Hmm, how about a joke instead? Just say 'Tell me a joke!'",
            "🧠 Not sure what you mean, but want a random fact? Ask for 'an interesting fact!'",
            "💭 I didn't catch that, but I can inspire you! Try 'Give me a quote!'"
        ]
        return random.choice(suggestions)

# Sidebar with API controls
st.sidebar.header("🌐 API Control Center")

# Location setting
st.sidebar.subheader("📍 Your Location")
new_location = st.sidebar.text_input("City for weather:", value=st.session_state.user_location)
if new_location != st.session_state.user_location:
    st.session_state.user_location = new_location

# API Statistics
st.sidebar.subheader("📊 API Usage Today")
stats = st.session_state.api_usage_stats
st.sidebar.metric("Total API Calls", stats['total_api_calls'])
st.sidebar.metric("Weather Requests", stats['weather_calls'])
st.sidebar.metric("Jokes Fetched", stats['jokes_fetched'])
st.sidebar.metric("Facts Retrieved", stats['facts_retrieved'])
st.sidebar.metric("Quotes Shared", stats['quotes_shared'])

# Quick action buttons
st.sidebar.subheader("⚡ Quick Actions")
col1, col2 = st.sidebar.columns(2)

with col1:
    if st.button("🌤️ Weather"):
        weather_response = get_weather_data(st.session_state.user_location)
        st.session_state.messages.append({"role": "user", "content": "What's the weather?"})
        st.session_state.messages.append({"role": "assistant", "content": weather_response})
        st.rerun()
    
    if st.button("🧠 Random Fact"):
        fact_response = get_random_fact()
        st.session_state.messages.append({"role": "user", "content": "Tell me a fact"})
        st.session_state.messages.append({"role": "assistant", "content": fact_response})
        st.rerun()

with col2:
    if st.button("😄 Random Joke"):
        joke_response = get_random_joke()
        st.session_state.messages.append({"role": "user", "content": "Tell me a joke"})
        st.session_state.messages.append({"role": "assistant", "content": joke_response})
        st.rerun()
    
    if st.button("💭 Inspiration"):
        quote_response = get_inspirational_quote()
        st.session_state.messages.append({"role": "user", "content": "Inspire me"})
        st.session_state.messages.append({"role": "assistant", "content": quote_response})
        st.rerun()

# Connection status
st.sidebar.markdown("---")
st.sidebar.subheader("🔌 Connection Status")
st.sidebar.success("🌐 Internet Connected")
st.sidebar.info("⚡ All APIs Operational")

# Main chat interface
col1, col2 = st.columns([2, 1])

with col1:
    st.header("💬 Chat with API Powers")
    
    # Display messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Chat input with loading
    if prompt := st.chat_input("Ask me about weather, jokes, facts, or inspiration!"):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Show thinking message briefly
        with st.chat_message("assistant"):
            with st.spinner("🌐 Fetching from the internet..."):
                time.sleep(0.3)  # Brief delay for effect
                bot_response = get_smart_response(prompt)
        
        # Add bot response
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        
        st.rerun()

with col2:
    st.header("🧪 API Testing Lab")
    
    # API tester
    st.subheader("Test Individual APIs")
    
    if st.button("🧪 Test Weather API", use_container_width=True):
        with st.spinner("Testing weather API..."):
            result = get_weather_data(st.session_state.user_location)
            st.success(result)
    
    if st.button("🧪 Test Joke API", use_container_width=True):
        with st.spinner("Testing joke API..."):
            result = get_random_joke()
            st.success(result)
    
    if st.button("🧪 Test Facts API", use_container_width=True):
        with st.spinner("Testing facts API..."):
            result = get_random_fact()
            st.success(result)
    
    # Example requests
    st.subheader("💡 Try These Requests")
    example_requests = [
        "What's the weather in London?",
        "Tell me a programming joke",
        "Give me an interesting fact",
        "I need some inspiration",
        "What's the weather like?",
        "Make me laugh!",
        "Teach me something cool"
    ]
    
    for example in example_requests:
        if st.button(f"💬 \"{example}\"", key=example):
            st.session_state.messages.append({"role": "user", "content": example})
            bot_response = get_smart_response(example)
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
            st.rerun()

# Clear chat functionality
if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "🌐 Fresh start! I'm ready to connect you to the world again! What would you like to know? 🚀"
    })
    st.rerun()

# Footer
st.markdown("---")
st.success("""
**🎯 Day 3 Challenge**: Can you add these API features?
- Add a news API for latest headlines
- Create a translation service
- Build a unit converter (temperature, currency, etc.)
- Add a random recipe finder
- Integrate a cat/dog picture API for fun!
""")

"""
🚀 Tomorrow: We'll save all this API-powered conversation data to a permanent database!
"""