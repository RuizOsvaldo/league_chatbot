"""
Day 2 Example: Adding Personality & Intelligence
The LEAGUE of Amazing Programmers

Make your chatbot smart and give it personality!
Run: streamlit run day_2_example.py
"""

import streamlit as st
import random
from datetime import datetime

# Page setup
st.set_page_config(
    page_title="Smart Chatbot",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Day 2: Smart Chatbot with Personality")
st.write("Today we're making our bot smarter and more fun!")

# Initialize session state for chat and bot personality
if 'messages' not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Yo! I'm your upgraded chatbot! 🎉 I've got personality now! Try asking me about my mood, telling me a joke, or just chat!"
    })

if 'bot_mood' not in st.session_state:
    st.session_state.bot_mood = "happy"
    
if 'user_name' not in st.session_state:
    st.session_state.user_name = None

if 'joke_count' not in st.session_state:
    st.session_state.joke_count = 0

# Bot personality settings
MOODS = {
    "happy": {"emoji": "😊", "style": "cheerful and enthusiastic"},
    "excited": {"emoji": "🤩", "style": "super energetic"},
    "chill": {"emoji": "😎", "style": "relaxed and cool"},
    "silly": {"emoji": "🤪", "style": "goofy and playful"},
    "sleepy": {"emoji": "😴", "style": "tired but friendly"}
}

# Joke collection
JOKES = [
    "Why don't scientists trust atoms? Because they make up everything! 🤣",
    "What do you call a bear with no teeth? A gummy bear! 🐻",
    "Why did the scarecrow win an award? He was outstanding in his field! 🌾",
    "What do you call a fake noodle? An impasta! 🍝",
    "Why did the math book look so sad? Because it had too many problems! 📚",
    "What do you call a dinosaur that crashes his car? Tyrannosaurus Wrecks! 🦕",
    "Why can't a bicycle stand up by itself? It's two tired! 🚴",
    "What did the ocean say to the beach? Nothing, it just waved! 🌊"
]

# Fun facts collection
FUN_FACTS = [
    "🐙 Octopuses have three hearts and blue blood!",
    "🍯 Honey never spoils - archaeologists have found 3000-year-old honey that's still edible!",
    "🎮 The first video game was created in 1958 - it was a tennis game!",
    "💤 You can't sneeze in your sleep because your sneeze reflexes are turned off!",
    "🍕 Pizza was originally considered peasant food in Italy!",
    "🦒 A giraffe's tongue is about 20 inches long!",
    "⚡ Lightning strikes the Earth about 100 times per second!",
    "🌙 Footprints on the moon will last millions of years!"
]

def get_bot_response(user_input):
    """Generate intelligent responses based on user input and bot mood"""
    user_input_lower = user_input.lower()
    current_mood = MOODS[st.session_state.bot_mood]
    
    # Check if user is telling their name
    if st.session_state.user_name is None:
        if "my name is" in user_input_lower or "i'm " in user_input_lower or "i am " in user_input_lower:
            # Try to extract the name
            if "my name is" in user_input_lower:
                name = user_input.split("my name is")[-1].strip().split()[0]
            elif "i'm " in user_input_lower:
                name = user_input.split("i'm ")[-1].strip().split()[0]
            else:
                name = user_input.split("i am ")[-1].strip().split()[0]
            
            st.session_state.user_name = name.capitalize()
            return f"Nice to meet you, {st.session_state.user_name}! {current_mood['emoji']} That's a cool name!"
    
    # Personalized responses if we know the user's name
    name_greeting = f", {st.session_state.user_name}" if st.session_state.user_name else ""
    
    # Mood-related responses
    if "mood" in user_input_lower or "feeling" in user_input_lower:
        return f"I'm feeling {st.session_state.bot_mood}{name_greeting}! {current_mood['emoji']} Want to hear a joke to match my mood?"
    
    # Change bot's mood
    if "be happy" in user_input_lower:
        st.session_state.bot_mood = "happy"
        return f"You got it{name_greeting}! 😊 I'm happy now! Life is good!"
    elif "be excited" in user_input_lower:
        st.session_state.bot_mood = "excited"
        return f"YESSS{name_greeting}! 🤩 I'M SO PUMPED RIGHT NOW! EVERYTHING IS AWESOME!"
    elif "be chill" in user_input_lower or "be cool" in user_input_lower:
        st.session_state.bot_mood = "chill"
        return f"No worries{name_greeting}, I'm chillin' now 😎 Everything's cool..."
    elif "be silly" in user_input_lower:
        st.session_state.bot_mood = "silly"
        return f"Time to get GOOFY{name_greeting}! 🤪 Beep boop banana phone!"
    
    # Joke responses
    if "joke" in user_input_lower or "funny" in user_input_lower:
        st.session_state.joke_count += 1
        joke = random.choice(JOKES)
        if st.session_state.joke_count > 3:
            return f"Another one{name_greeting}? You really love jokes! Here goes: {joke}"
        return f"Here's one for you{name_greeting}: {joke}"
    
    # Fun fact responses
    if "fact" in user_input_lower or "interesting" in user_input_lower:
        fact = random.choice(FUN_FACTS)
        return f"Here's something cool{name_greeting}: {fact}"
    
    # Game suggestions
    if "bored" in user_input_lower or "game" in user_input_lower:
        games = [
            "Let's play 20 questions! Think of something and I'll try to guess!",
            "How about a riddle? I'll tell you one!",
            "Want to hear some fun facts? Just ask!",
            "Let's see how many jokes you can handle! 😄"
        ]
        return f"{random.choice(games)}"
    
    # Math help
    if any(op in user_input for op in ['+', '-', '*', '/']):
        try:
            # Safety: only evaluate simple math
            if all(c in '0123456789+-*/.() ' for c in user_input):
                result = eval(user_input)
                return f"That equals {result}! {current_mood['emoji']} Math is fun!"
        except:
            return f"Hmm, that math looks tricky{name_greeting}! Try something like '2 + 2' or '10 * 5'"
    
    # Time-based responses
    if "time" in user_input_lower or "what's the time" in user_input_lower:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"It's {current_time}{name_greeting}! {current_mood['emoji']}"
    
    # Greeting responses based on mood
    if any(greet in user_input_lower for greet in ["hello", "hi", "hey", "sup"]):
        greetings = {
            "happy": f"Hey there{name_greeting}! 😊 So glad you're here!",
            "excited": f"OMG HI{name_greeting}! 🤩 THIS IS AMAZING!",
            "chill": f"Sup{name_greeting} 😎 How's it hanging?",
            "silly": f"HELLO-JELLO-BANANA-FELLOW{name_greeting}! 🤪",
            "sleepy": f"*yawn* Oh hey{name_greeting}... 😴 What's up?"
        }
        return greetings[st.session_state.bot_mood]
    
    # Default responses based on mood
    defaults = {
        "happy": [
            f"That's awesome{name_greeting}! Tell me more! 😊",
            f"I love hearing about that{name_greeting}! 😄",
            f"You're making me even happier{name_greeting}! 🌟"
        ],
        "excited": [
            f"OMG THAT'S SO COOL{name_greeting}! 🤩",
            f"I CAN'T EVEN RIGHT NOW{name_greeting}! 🎉",
            f"THIS IS THE BEST THING EVER{name_greeting}! 🚀"
        ],
        "chill": [
            f"Cool, cool{name_greeting}... 😎",
            f"That's pretty chill{name_greeting} 👌",
            f"Nice vibes{name_greeting} ✨"
        ],
        "silly": [
            f"Banana hammock{name_greeting}! Wait, what were we talking about? 🤪",
            f"That reminds me of a dancing pickle{name_greeting}! 🥒",
            f"Beep boop{name_greeting}, does not compute... just kidding! 🤖"
        ],
        "sleepy": [
            f"*yawn* That's nice{name_greeting}... 😴",
            f"Mmhmm... *rubs eyes* ...go on{name_greeting}... 😪",
            f"I'm listening{name_greeting}... just resting my eyes... 💤"
        ]
    }
    
    return random.choice(defaults[st.session_state.bot_mood])

# Sidebar with bot controls
st.sidebar.header("🎮 Bot Controls")
st.sidebar.write(f"**Current Mood**: {st.session_state.bot_mood} {MOODS[st.session_state.bot_mood]['emoji']}")

# Mood selector
new_mood = st.sidebar.selectbox(
    "Change bot mood:",
    list(MOODS.keys()),
    index=list(MOODS.keys()).index(st.session_state.bot_mood)
)
if new_mood != st.session_state.bot_mood:
    st.session_state.bot_mood = new_mood
    st.rerun()

# Stats
st.sidebar.markdown("---")
st.sidebar.header("📊 Chat Stats")
if st.session_state.user_name:
    st.sidebar.write(f"**Chatting with**: {st.session_state.user_name}")
st.sidebar.metric("Total Messages", len(st.session_state.messages))
st.sidebar.metric("Jokes Told", st.session_state.joke_count)

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("Say something..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Get bot response
    bot_response = get_bot_response(prompt)
    
    # Add bot response
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    
    st.rerun()

# Clear chat button
if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.session_state.user_name = None
    st.session_state.joke_count = 0
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Fresh start! I'm ready for a new conversation! What's your name? 😊"
    })
    st.rerun()

# Commands help
with st.expander("💡 Bot Commands & Features"):
    st.markdown("""
    **Things to try:**
    - Tell me your name: "My name is [your name]"
    - Ask for a joke: "Tell me a joke"
    - Get a fun fact: "Tell me something interesting"
    - Check my mood: "How are you feeling?"
    - Change my mood: "Be silly" / "Be excited" / "Be chill"
    - Do math: Type any math problem like "5 + 3"
    - Ask the time: "What time is it?"
    - Say you're bored: "I'm bored"
    
    **Moods available:**
    - 😊 Happy (default)
    - 🤩 Excited
    - 😎 Chill
    - 🤪 Silly
    - 😴 Sleepy
    """)

# Footer
st.markdown("---")
st.success("""
**🎯 Day 2 Challenge**: Can you add these features?
- Add a "confused" mood with appropriate responses
- Make the bot remember your favorite color
- Add riddles in addition to jokes
- Create a simple guessing game
""")

"""
🚀 Tomorrow: We'll add visual analytics and make our bot even cooler with charts and data tracking!
"""