"""
Day 5 Template: Add Games & Advanced Features
The LEAGUE of Amazing Programmers

Make your chatbot fun with games, commands, and special features!
Run: streamlit run day_5.py
"""

import streamlit as st
import sqlite3
import pandas as pd
import random
import json
from datetime import datetime
import time

# TODO 1: Set up page configuration
# page_title="Advanced Chatbot"
# page_icon="🎮"
# layout="wide"
# YOUR CODE HERE:


# TODO 2: Create title and description
# Emphasize games and special commands
# YOUR CODE HERE:


# TODO 3: Enhanced database initialization
def init_enhanced_database():
    """Initialize database with game tables"""
    conn = sqlite3.connect('chatbot_advanced.db')
    cursor = conn.cursor()
    
    # TODO 4: Create game_scores table
    # Columns:
    # - id (INTEGER PRIMARY KEY AUTOINCREMENT)
    # - username (TEXT)
    # - game_type (TEXT)
    # - score (INTEGER)
    # - timestamp (DATETIME DEFAULT CURRENT_TIMESTAMP)
    # YOUR CODE HERE:
    
    # TODO 5: Create achievements table
    # Columns:
    # - id (INTEGER PRIMARY KEY AUTOINCREMENT)
    # - username (TEXT)
    # - achievement_name (TEXT)
    # - earned_at (DATETIME DEFAULT CURRENT_TIMESTAMP)
    # - description (TEXT)
    # YOUR CODE HERE:
    
    # TODO 6: Create quiz_questions table
    # Columns:
    # - id (INTEGER PRIMARY KEY AUTOINCREMENT)
    # - category (TEXT)
    # - question (TEXT)
    # - correct_answer (TEXT)
    # - wrong_answers (TEXT) [JSON array]
    # - difficulty (TEXT)
    # YOUR CODE HERE:
    
    conn.commit()
    conn.close()


# TODO 7: Initialize enhanced database
# YOUR CODE HERE:


# TODO 8: Define command system
COMMANDS = {
    '/help': 'Show all commands',
    '/play': 'Start a game',
    '/quiz': 'Start a quiz',
    '/joke': 'Tell a joke',
    '/fact': 'Share a fun fact',
    # TODO: Add more commands
}


# TODO 9: Initialize session state for games
# Add:
# - current_game (what game is active)
# - game_data (game-specific data)
# - user_score (current session score)
# - achievements (list of earned achievements)
# YOUR CODE HERE:


# TODO 10: Create number guessing game
def start_number_game():
    """Start a number guessing game"""
    # TODO: Implement number game
    # - Generate random number 1-100
    # - Store in session state
    # - Return instructions
    # YOUR CODE HERE:
    pass


def process_number_guess(guess):
    """Process a guess in number game"""
    # TODO: Implement guess processing
    # - Check if correct
    # - Give hints (higher/lower)
    # - Track attempts
    # - Award points
    # - Save score to database
    # YOUR CODE HERE:
    pass


# TODO 11: Create quiz game
def start_quiz():
    """Start a quiz with random question"""
    # TODO: Implement quiz start
    # - Get random question from database
    # - Shuffle answers
    # - Store in session state
    # - Return formatted question
    # YOUR CODE HERE:
    pass


def process_quiz_answer(answer):
    """Process quiz answer"""
    # TODO: Check answer
    # - Compare with correct answer
    # - Award points if correct
    # - Save score
    # - Return result message
    # YOUR CODE HERE:
    pass


# TODO 12: Create word game
def start_word_game():
    """Start a word guessing game"""
    # TODO: Implement word game
    # - Choose random word
    # - Show blanks or scrambled letters
    # - Store in session state
    # YOUR CODE HERE:
    pass


# TODO 13: Create trivia game
def start_trivia():
    """Start trivia questions"""
    # TODO: Implement trivia
    # - Multiple choice questions
    # - Different categories
    # - Difficulty levels
    # YOUR CODE HERE:
    pass


# TODO 14: Create command processor
def process_command(command, args=""):
    """Process special commands"""
    command = command.lower()
    
    # TODO 15: Implement /help command
    # Return list of all available commands
    # YOUR CODE HERE:
    
    # TODO 16: Implement /play command
    # Let user choose a game or random
    # YOUR CODE HERE:
    
    # TODO 17: Implement /joke command
    # Return random joke
    # YOUR CODE HERE:
    
    # TODO 18: Implement /fact command
    # Return random fun fact
    # YOUR CODE HERE:
    
    # TODO 19: Implement /stats command
    # Show user statistics
    # YOUR CODE HERE:
    
    # TODO 20: Add more commands
    # Ideas:
    # - /8ball (magic 8-ball)
    # - /roll (dice roller)
    # - /flip (coin flip)
    # - /timer (countdown timer)
    # - /todo (todo list)
    # YOUR CODE HERE:
    
    return "Unknown command. Type /help for available commands."


# TODO 21: Create achievement system
def check_achievement(username, action):
    """Check and award achievements"""
    # TODO: Implement achievements
    # Examples:
    # - "First Game": Play your first game
    # - "Quiz Master": Answer 5 quiz questions correctly
    # - "Persistent": Chat for 5 days in a row
    # - "High Scorer": Score over 100 points
    # YOUR CODE HERE:
    pass


def save_achievement(username, achievement_name, description):
    """Save achievement to database"""
    # TODO: Save to achievements table
    # YOUR CODE HERE:
    pass


# TODO 22: Create leaderboard functions
def get_leaderboard(game_type=None):
    """Get top scores from database"""
    # TODO: Query game_scores table
    # - Filter by game_type if specified
    # - Order by score DESC
    # - Limit to top 10
    # - Return as DataFrame
    # YOUR CODE HERE:
    return pd.DataFrame()


# TODO 23: Create main response handler
def get_bot_response(user_input):
    """Main response handler with game support"""
    # TODO: Check if in a game first
    # If in game, process game input
    # YOUR CODE HERE:
    
    # TODO: Check for commands (start with /)
    # Process commands
    # YOUR CODE HERE:
    
    # TODO: Regular chat responses
    # YOUR CODE HERE:
    
    return "Let's play a game! Type /help for commands."


# TODO 24: Create sidebar with game info
# Show:
# - Current game (if active)
# - Session score
# - Achievements earned
# - Quick command buttons
# YOUR CODE HERE:


# TODO 25: Create main chat interface
# Display messages
# Handle input
# Process games and commands
# YOUR CODE HERE:


# TODO 26: Create leaderboard tab
# Show:
# - Top scores for each game
# - User's rank
# - Recent achievements
# YOUR CODE HERE:


# TODO 27: Create achievements tab
# Display:
# - All available achievements
# - Which ones user has earned
# - Progress towards next achievement
# YOUR CODE HERE:


# TODO 28: Add special effects
# Choose at least 2:
# - Confetti for achievements (st.balloons())
# - Sound effects for games
# - Animated score counter
# - Streak tracker
# - Daily challenges
# YOUR CODE HERE:


# TODO 29: Create game statistics
# Track and display:
# - Games played
# - Win rate
# - Average score
# - Favorite game
# - Best streak
# YOUR CODE HERE:


# TODO 30: Polish game experience
# Add:
# - Difficulty levels
# - Hints system
# - Multiplayer simulation
# - Tournament mode
# - Practice mode
# YOUR CODE HERE:


"""
🎯 Challenges when complete:
1. Create a RPG-style leveling system
2. Add mini-games like tic-tac-toe or hangman
3. Create daily challenges with rewards
4. Add a virtual pet that grows with interaction
5. Build a story adventure game

💡 Game Design Tips:
- Keep games simple but engaging
- Provide clear instructions
- Give immediate feedback
- Balance difficulty
- Reward participation, not just winning
- Add variety to maintain interest

When complete, your chatbot should:
✅ Play multiple games
✅ Process special commands
✅ Track scores and achievements
✅ Show leaderboards
✅ Award achievements
✅ Remember game statistics
✅ Provide entertainment value
✅ Keep users engaged
"""