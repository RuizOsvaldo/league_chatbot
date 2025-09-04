"""
Day 3 Template: Connect Your Bot to the Real World!
The LEAGUE of Amazing Programmers

Add external APIs to make your chatbot truly intelligent and useful.
Run: streamlit run day_3.py
"""

import streamlit as st
import requests
import json
import random
from datetime import datetime, timedelta
import time

# TODO 1: Set up page with API focus
# Use st.set_page_config() with:
# - page_title="API-Powered Chatbot"
# - page_icon="🌐"
# - layout="centered"
# YOUR CODE HERE:


# TODO 2: Create title and description
# Emphasize connecting to real-world data and services
# YOUR CODE HERE:


# TODO 3: Initialize session state for API features
# You'll need:
# - messages (list)
# - user_location (string, default "New York")
# - api_usage_stats (dictionary)
# - favorite_apis (list)
# YOUR CODE HERE:
if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'api_usage_stats' not in st.session_state:
    st.session_state.api_usage_stats = {
        'weather_calls': 0,
        'jokes_fetched': 0,
        'facts_retrieved': 0,
        'news_requests': 0
    }


# TODO 4: Create weather API function
def get_weather_data(city="New York"):
    """Get weather data from a free API"""
    try:
        # TODO: Implement weather API call
        # Use a free service like OpenWeatherMap or weatherapi.com
        # Handle API key if needed (store in secrets)
        # Return formatted weather string
        # Example response: "It's 72°F and sunny in New York"
        # YOUR CODE HERE:
        
        # Placeholder response for now
        return f"Weather API not implemented yet for {city}"
    except Exception as e:
        return f"Sorry, couldn't get weather data: {str(e)}"


# TODO 5: Create joke API function
def get_random_joke():
    """Fetch a random joke from an API"""
    try:
        # TODO: Use a joke API like:
        # - https://official-joke-api.appspot.com/random_joke
        # - https://sv443.net/jokeapi/v2/joke/Any
        # Parse the response and format nicely
        # YOUR CODE HERE:
        
        # Placeholder jokes
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything! 😄",
            "What do you call a fake noodle? An impasta! 🍝",
            "Why did the scarecrow win an award? He was outstanding in his field! 🌾"
        ]
        return random.choice(jokes)
    except Exception as e:
        return f"Joke API failed: {str(e)}"


# TODO 6: Create fun facts API function
def get_random_fact():
    """Get a random interesting fact"""
    try:
        # TODO: Use APIs like:
        # - http://numbersapi.com/random/trivia
        # - https://uselessfacts.jsph.pl/random.json
        # - https://api.api-ninjas.com/v1/facts
        # YOUR CODE HERE:
        
        # Placeholder facts
        facts = [
            "🐙 Octopuses have three hearts and blue blood!",
            "🍯 Honey never spoils - archaeologists have found 3000-year-old edible honey!",
            "🌙 Footprints on the moon will last millions of years!"
        ]
        return random.choice(facts)
    except Exception as e:
        return f"Facts API failed: {str(e)}"


# TODO 7: Create news headlines function
def get_latest_news(category="general"):
    """Get latest news headlines"""
    try:
        # TODO: Use news APIs like:
        # - https://newsapi.org (requires free API key)
        # - https://api.currentsapi.services/v1/latest-news
        # Filter by category if needed
        # YOUR CODE HERE:
        
        # Placeholder news
        return "📰 News API not implemented yet. Check back later!"
    except Exception as e:
        return f"News API failed: {str(e)}"


# TODO 8: Create currency converter function
def convert_currency(amount, from_currency, to_currency):
    """Convert between currencies"""
    try:
        # TODO: Use currency APIs like:
        # - https://api.exchangerate-api.com/v4/latest/USD
        # - https://api.fixer.io/latest
        # Calculate conversion and return formatted result
        # YOUR CODE HERE:
        
        return f"Currency conversion not implemented yet"
    except Exception as e:
        return f"Currency API failed: {str(e)}"


# TODO 9: Create random quote function
def get_inspirational_quote():
    """Get a motivational quote"""
    try:
        # TODO: Use quote APIs like:
        # - https://api.quotable.io/random
        # - https://zenquotes.io/api/random
        # Format nicely with author
        # YOUR CODE HERE:
        
        quotes = [
            '"The only way to do great work is to love what you do." - Steve Jobs',
            '"Innovation distinguishes between a leader and a follower." - Steve Jobs',
            '"Code is like humor. When you have to explain it, it\'s bad." - Cory House'
        ]
        return random.choice(quotes)
    except Exception as e:
        return f"Quote API failed: {str(e)}"


# TODO 10: Create API response handler
def handle_api_request(user_input):
    """Determine which API to call based on user input"""
    user_input_lower = user_input.lower()
    
    # TODO 11: Weather requests
    if any(word in user_input_lower for word in ['weather', 'temperature', 'forecast', 'rain', 'sunny']):
        # Extract city name if mentioned
        # Default to user's location
        # Update usage stats
        # YOUR CODE HERE:
        st.session_state.api_usage_stats['weather_calls'] += 1
        return get_weather_data()
    
    # TODO 12: Joke requests
    elif any(word in user_input_lower for word in ['joke', 'funny', 'laugh', 'humor']):
        # YOUR CODE HERE:
        st.session_state.api_usage_stats['jokes_fetched'] += 1
        return get_random_joke()
    
    # TODO 13: Fact requests
    elif any(word in user_input_lower for word in ['fact', 'interesting', 'learn', 'trivia']):
        # YOUR CODE HERE:
        st.session_state.api_usage_stats['facts_retrieved'] += 1
        return get_random_fact()
    
    # TODO 14: News requests
    elif any(word in user_input_lower for word in ['news', 'headlines', 'current events']):
        # YOUR CODE HERE:
        st.session_state.api_usage_stats['news_requests'] += 1
        return get_latest_news()
    
    # TODO 15: Quote requests
    elif any(word in user_input_lower for word in ['quote', 'inspiration', 'motivate']):
        # YOUR CODE HERE:
        return get_inspirational_quote()
    
    # TODO 16: Currency conversion
    elif 'convert' in user_input_lower and any(curr in user_input_lower for curr in ['usd', 'eur', 'gbp', 'dollar', 'euro']):
        # Parse amounts and currencies from input
        # YOUR CODE HERE:
        return convert_currency(100, 'USD', 'EUR')
    
    return None  # No API match found


# TODO 17: Create enhanced response system
def get_smart_api_response(user_input):
    """Generate responses with API integration"""
    
    # First, try to handle with APIs
    api_response = handle_api_request(user_input)
    if api_response:
        return api_response
    
    # TODO 18: Regular chat responses with API suggestions
    user_input_lower = user_input.lower()
    
    if any(word in user_input_lower for word in ['hello', 'hi', 'hey']):
        return "Hi there! 🌐 I'm connected to the internet now! Try asking me about the weather, for a joke, or some interesting facts!"
    
    elif 'help' in user_input_lower:
        return """🌐 I can help you with:
        
**Weather** 🌤️ - "What's the weather?" or "How's the weather in Tokyo?"
**Jokes** 😄 - "Tell me a joke" or "Make me laugh"
**Facts** 🧠 - "Give me a fact" or "Something interesting"
**News** 📰 - "What's in the news?" or "Latest headlines"
**Quotes** 💭 - "Inspire me" or "Give me a quote"
**Currency** 💱 - "Convert 100 USD to EUR"

Just ask naturally!"""
    
    elif 'what can you do' in user_input_lower:
        return "I'm connected to the internet! I can get real-time weather, fetch jokes, find interesting facts, get news headlines, and more! What would you like to try?"
    
    else:
        # TODO 19: Suggest API features for unclear requests
        suggestions = [
            "I'm not sure about that, but I can get you the weather! ☀️",
            "Hmm, how about a random fact instead? 🤔",
            "Not sure what you mean, but want to hear a joke? 😄",
            "I didn't understand, but I can check the news for you! 📰"
        ]
        return random.choice(suggestions)


# TODO 20: Create sidebar with API controls
# Add:
# - Location selector for weather
# - API usage statistics
# - Quick action buttons
# - Connection status indicators
# YOUR CODE HERE:


# TODO 21: Create main chat interface
# Display messages with API-enhanced responses
# Handle user input with API integration
# Show loading states for API calls
# YOUR CODE HERE:


# TODO 22: Create API testing panel
# Add a section where students can:
# - Test individual APIs
# - See raw API responses
# - Debug API issues
# - Monitor API usage
# YOUR CODE HERE:


# TODO 23: Add error handling and fallbacks
def safe_api_call(api_function, *args, **kwargs):
    """Safely call API with fallback responses"""
    try:
        # TODO: Implement with timeout
        # Add retry logic
        # Return formatted response
        # YOUR CODE HERE:
        return api_function(*args, **kwargs)
    except requests.exceptions.Timeout:
        return "⏰ That request timed out. Please try again!"
    except requests.exceptions.ConnectionError:
        return "🌐 Couldn't connect to the internet. Check your connection!"
    except Exception as e:
        return f"❌ Something went wrong: {str(e)}"


# TODO 24: Create API rate limiting
# Implement basic rate limiting to avoid hitting API limits
# Track calls per hour/day
# Show warnings when approaching limits
# YOUR CODE HERE:


# TODO 25: Add API configuration
# Allow users to:
# - Add their own API keys
# - Choose preferred services
# - Enable/disable specific APIs
# - Set default locations/preferences
# YOUR CODE HERE:


"""
🎯 Challenges when complete:
1. Add more APIs (sports scores, stock prices, recipes)
2. Create a location-aware weather system
3. Build a news reader with article summaries
4. Add image APIs for visual responses
5. Create a translator using Google Translate API

💡 API Integration Tips:
- Always handle errors gracefully
- Use free APIs when possible (no API keys needed)
- Cache responses to avoid repeated calls
- Show loading states for slow APIs
- Provide fallback responses when APIs fail
- Respect rate limits

🌐 Recommended Free APIs:
- Weather: OpenWeatherMap, WeatherAPI
- Jokes: JokeAPI, Official Joke API
- Facts: NumbersAPI, Useless Facts API
- News: NewsAPI (limited free tier)
- Quotes: Quotable, ZenQuotes
- Currency: ExchangeRate-API, Fixer.io

When complete, your chatbot should:
✅ Connect to real-world data sources
✅ Provide live weather information
✅ Fetch jokes and facts on demand
✅ Show latest news headlines
✅ Handle API errors gracefully
✅ Track API usage statistics
✅ Feel connected to the real world
✅ Be genuinely useful for information
"""