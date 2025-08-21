"""
Day 5 Example: Advanced Chatbot Features
The LEAGUE of Amazing Programmers

Add games, quizzes, and special commands to your chatbot!
Run: streamlit run day_5_example.py
"""

import streamlit as st
import sqlite3
import pandas as pd
import random
import json
from datetime import datetime
import time

# Page setup
st.set_page_config(
    page_title="Advanced Chatbot",
    page_icon="🎮",
    layout="wide"
)

st.title("🎮 Day 5: Advanced Chatbot Features")
st.write("Games, quizzes, commands, and more!")

# Database initialization (enhanced from Day 4)
def init_database():
    """Initialize enhanced database with game tables"""
    conn = sqlite3.connect('chatbot_advanced.db')
    cursor = conn.cursor()
    
    # Messages table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            role TEXT,
            content TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            command_used TEXT
        )
    ''')
    
    # Game scores table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS game_scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            game_type TEXT,
            score INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Quiz questions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quiz_questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            question TEXT,
            correct_answer TEXT,
            wrong_answers TEXT,
            difficulty TEXT
        )
    ''')
    
    # User achievements table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS achievements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            achievement TEXT,
            earned_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Add sample quiz questions if empty
    cursor.execute("SELECT COUNT(*) FROM quiz_questions")
    if cursor.fetchone()[0] == 0:
        sample_questions = [
            ('general', 'What is the capital of France?', 'Paris', '["London", "Berlin", "Madrid"]', 'easy'),
            ('general', 'How many continents are there?', '7', '["5", "6", "8"]', 'easy'),
            ('tech', 'What does CPU stand for?', 'Central Processing Unit', '["Computer Personal Unit", "Central Program Utility", "Core Processing Unit"]', 'easy'),
            ('tech', 'What year was Python created?', '1991', '["1989", "1995", "2000"]', 'medium'),
            ('science', 'What is H2O?', 'Water', '["Hydrogen", "Oxygen", "Helium"]', 'easy'),
            ('science', 'How many planets are in our solar system?', '8', '["7", "9", "10"]', 'easy'),
            ('gaming', 'What year was Minecraft released?', '2011', '["2009", "2013", "2015"]', 'medium'),
            ('gaming', 'Who created Super Mario?', 'Nintendo', '["Sega", "Sony", "Microsoft"]', 'easy')
        ]
        cursor.executemany(
            'INSERT INTO quiz_questions (category, question, correct_answer, wrong_answers, difficulty) VALUES (?, ?, ?, ?, ?)',
            sample_questions
        )
    
    conn.commit()
    conn.close()

# Initialize database
init_database()

# Session state initialization
if 'messages' not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "🎮 Welcome to the Advanced Chatbot! I can play games, give quizzes, and respond to special commands! Type /help to see what I can do!"
    })

if 'current_game' not in st.session_state:
    st.session_state.current_game = None

if 'game_data' not in st.session_state:
    st.session_state.game_data = {}

if 'user_name' not in st.session_state:
    st.session_state.user_name = "Player"

if 'user_score' not in st.session_state:
    st.session_state.user_score = 0

if 'achievements' not in st.session_state:
    st.session_state.achievements = []

# Command system
COMMANDS = {
    '/help': 'Show all available commands',
    '/play': 'Start a game (number guessing, trivia, or word game)',
    '/quiz': 'Start a quiz',
    '/joke': 'Tell a random joke',
    '/fact': 'Share a fun fact',
    '/stats': 'Show your statistics',
    '/achievements': 'View your achievements',
    '/clear': 'Clear the chat',
    '/mood': 'Check bot mood',
    '/8ball': 'Ask the magic 8-ball',
    '/roll': 'Roll dice (e.g., /roll 2d6)',
    '/flip': 'Flip a coin',
    '/timer': 'Set a timer (e.g., /timer 5)',
    '/todo': 'Manage your todo list'
}

# Game functions
def start_number_game():
    """Start a number guessing game"""
    st.session_state.current_game = 'number_guess'
    st.session_state.game_data = {
        'target': random.randint(1, 100),
        'attempts': 0,
        'max_attempts': 7
    }
    return "🔢 I'm thinking of a number between 1 and 100! You have 7 guesses. What's your first guess?"

def process_number_guess(guess_str):
    """Process a guess in the number game"""
    try:
        guess = int(guess_str)
        game_data = st.session_state.game_data
        game_data['attempts'] += 1
        
        if guess == game_data['target']:
            score = (game_data['max_attempts'] - game_data['attempts'] + 1) * 10
            save_game_score(st.session_state.user_name, 'number_guess', score)
            st.session_state.user_score += score
            st.session_state.current_game = None
            check_achievement('number_master', 'Won a number guessing game')
            return f"🎉 Correct! You got it in {game_data['attempts']} attempts! You earned {score} points!"
        elif guess < game_data['target']:
            remaining = game_data['max_attempts'] - game_data['attempts']
            if remaining > 0:
                return f"📈 Too low! Try higher. {remaining} guesses left."
            else:
                st.session_state.current_game = None
                return f"😔 Out of guesses! The number was {game_data['target']}. Better luck next time!"
        else:
            remaining = game_data['max_attempts'] - game_data['attempts']
            if remaining > 0:
                return f"📉 Too high! Try lower. {remaining} guesses left."
            else:
                st.session_state.current_game = None
                return f"😔 Out of guesses! The number was {game_data['target']}. Better luck next time!"
    except ValueError:
        return "Please enter a valid number!"

def start_quiz():
    """Start a quiz game"""
    conn = sqlite3.connect('chatbot_advanced.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM quiz_questions ORDER BY RANDOM() LIMIT 1')
    question_data = cursor.fetchone()
    conn.close()
    
    if question_data:
        st.session_state.current_game = 'quiz'
        wrong_answers = json.loads(question_data[4])
        all_answers = [question_data[3]] + wrong_answers
        random.shuffle(all_answers)
        
        st.session_state.game_data = {
            'question': question_data[2],
            'correct': question_data[3],
            'options': all_answers,
            'category': question_data[1]
        }
        
        options_text = "\n".join([f"{i+1}. {opt}" for i, opt in enumerate(all_answers)])
        return f"📚 **{question_data[1].upper()} QUIZ**\n\n{question_data[2]}\n\n{options_text}\n\nType the number of your answer!"
    
    return "No quiz questions available!"

def process_quiz_answer(answer_str):
    """Process a quiz answer"""
    try:
        answer_idx = int(answer_str) - 1
        if 0 <= answer_idx < len(st.session_state.game_data['options']):
            selected = st.session_state.game_data['options'][answer_idx]
            if selected == st.session_state.game_data['correct']:
                score = 15
                save_game_score(st.session_state.user_name, 'quiz', score)
                st.session_state.user_score += score
                st.session_state.current_game = None
                check_achievement('quiz_master', 'Answered a quiz question correctly')
                return f"✅ Correct! {st.session_state.game_data['correct']} is right! You earned {score} points! 🎉"
            else:
                st.session_state.current_game = None
                return f"❌ Wrong! The correct answer was: {st.session_state.game_data['correct']}"
        else:
            return "Please enter a number between 1 and " + str(len(st.session_state.game_data['options']))
    except ValueError:
        return "Please enter the number of your answer!"

def save_game_score(user, game_type, score):
    """Save game score to database"""
    conn = sqlite3.connect('chatbot_advanced.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO game_scores (user, game_type, score) VALUES (?, ?, ?)',
                   (user, game_type, score))
    conn.commit()
    conn.close()

def check_achievement(achievement_id, description):
    """Check and award achievements"""
    if achievement_id not in st.session_state.achievements:
        st.session_state.achievements.append(achievement_id)
        conn = sqlite3.connect('chatbot_advanced.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO achievements (user, achievement) VALUES (?, ?)',
                       (st.session_state.user_name, description))
        conn.commit()
        conn.close()
        st.balloons()
        return f"🏆 Achievement Unlocked: {description}!"
    return None

def process_command(command, args=""):
    """Process special commands"""
    command = command.lower()
    
    if command == '/help':
        help_text = "**Available Commands:**\n"
        for cmd, desc in COMMANDS.items():
            help_text += f"• `{cmd}` - {desc}\n"
        return help_text
    
    elif command == '/play':
        games = ['number', 'quiz', 'word']
        game_choice = random.choice(games)
        if game_choice == 'number':
            return start_number_game()
        elif game_choice == 'quiz':
            return start_quiz()
        else:
            return "🎮 Word game coming soon! Try /play again for a different game!"
    
    elif command == '/quiz':
        return start_quiz()
    
    elif command == '/joke':
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything! 😄",
            "What do you call a bear with no teeth? A gummy bear! 🐻",
            "Why did the scarecrow win an award? He was outstanding in his field! 🌾",
            "What do you call fake spaghetti? An impasta! 🍝",
            "Why did the bicycle fall over? It was two tired! 🚴"
        ]
        return random.choice(jokes)
    
    elif command == '/fact':
        facts = [
            "🐙 Octopuses have three hearts!",
            "🍯 Honey never spoils!",
            "⚡ Lightning strikes Earth 100 times per second!",
            "🦒 A giraffe's tongue is 20 inches long!",
            "🌙 Footprints on the moon last millions of years!"
        ]
        return random.choice(facts)
    
    elif command == '/stats':
        conn = sqlite3.connect('chatbot_advanced.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*), SUM(score) FROM game_scores WHERE user = ?',
                       (st.session_state.user_name,))
        games_played, total_score = cursor.fetchone()
        conn.close()
        
        return f"""📊 **Your Stats:**
        • Total Score: {total_score or 0} points
        • Games Played: {games_played or 0}
        • Current Session Score: {st.session_state.user_score}
        • Achievements: {len(st.session_state.achievements)}"""
    
    elif command == '/8ball':
        responses = [
            "Yes, definitely! ✨",
            "Ask again later... 🔮",
            "Cannot predict now 🌙",
            "Don't count on it 😬",
            "My sources say yes! 🌟",
            "Outlook not so good 😔",
            "Signs point to yes! ✅",
            "Very doubtful 🤔"
        ]
        return f"🎱 Magic 8-Ball says: {random.choice(responses)}"
    
    elif command == '/flip':
        result = random.choice(['Heads', 'Tails'])
        return f"🪙 Coin flip result: **{result}**!"
    
    elif command == '/roll':
        # Parse dice notation (e.g., 2d6)
        if args:
            try:
                parts = args.split('d')
                if len(parts) == 2:
                    num_dice = int(parts[0])
                    sides = int(parts[1])
                    rolls = [random.randint(1, sides) for _ in range(num_dice)]
                    total = sum(rolls)
                    return f"🎲 Rolled {args}: {rolls} = **{total}**"
            except:
                pass
        # Default single d6
        roll = random.randint(1, 6)
        return f"🎲 Rolled a d6: **{roll}**"
    
    elif command == '/clear':
        st.session_state.messages = []
        st.session_state.messages.append({
            "role": "assistant",
            "content": "💬 Chat cleared! Fresh start!"
        })
        return None  # Will trigger rerun
    
    else:
        return f"Unknown command: {command}. Type /help for available commands."

def get_bot_response(user_input):
    """Get bot response based on input"""
    # Check if in a game
    if st.session_state.current_game == 'number_guess':
        return process_number_guess(user_input)
    elif st.session_state.current_game == 'quiz':
        return process_quiz_answer(user_input)
    
    # Check for commands
    if user_input.startswith('/'):
        parts = user_input.split(' ', 1)
        command = parts[0]
        args = parts[1] if len(parts) > 1 else ""
        return process_command(command, args)
    
    # Regular responses
    user_input_lower = user_input.lower()
    
    if any(word in user_input_lower for word in ['hello', 'hi', 'hey']):
        return f"Hey {st.session_state.user_name}! 👋 Ready for some fun? Try /help to see what I can do!"
    elif 'how are you' in user_input_lower:
        return "I'm doing great! Full of games and ready to chat! Want to play something? Try /play! 🎮"
    elif any(word in user_input_lower for word in ['bye', 'goodbye']):
        return f"See you later, {st.session_state.user_name}! Your score of {st.session_state.user_score} points has been saved! 👋"
    else:
        return f"That's interesting! Want to try a game? Type /play or /help to see all my features! 🎮"

# Sidebar
st.sidebar.header("👤 Player Profile")

user_name = st.sidebar.text_input("Your name:", value=st.session_state.user_name)
if user_name != st.session_state.user_name:
    st.session_state.user_name = user_name
    st.rerun()

st.sidebar.metric("Session Score", st.session_state.user_score)
st.sidebar.metric("Achievements", len(st.session_state.achievements))

# Quick commands in sidebar
st.sidebar.markdown("---")
st.sidebar.header("⚡ Quick Commands")
for cmd in ['/play', '/quiz', '/joke', '/fact', '/stats']:
    if st.sidebar.button(cmd):
        st.session_state.messages.append({"role": "user", "content": cmd})
        response = process_command(cmd)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

# Main chat interface
st.header("💬 Advanced Chat Interface")

# Display messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("Type a message or command..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Get bot response
    response = get_bot_response(prompt)
    
    if response:  # None means clear command
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    st.rerun()

# Footer
st.markdown("---")
st.success("""
**🎯 Day 5 Challenge**: Can you add these features?
- Create a word guessing game
- Add a todo list command
- Build a math quiz mode
- Create custom achievements
""")

"""
🚀 Tomorrow: Final polish and deployment!
"""