"""
This module contains the predefined responses and patterns for the chatbot.
"""

# Greetings
GREETINGS_KEYWORDS = ["hi", "hello", "hey", "greetings", "wassup", "what's up"]
GREETINGS_RESPONSES = [
    "Hi there! How can I help you today?",
    "Hello! It's great to see you. How can I assist?",
    "Hey! I'm here to help you out.",
    "Greetings! What's on your mind today?"
]

# Questions about the bot
QUESTIONS_KEYWORDS = ["what", "how", "why"]
QUESTIONS_SPECIFIC = {
    "what is your name": ["I am SmartBot, your assistant.", "They call me SmartBot."],
    "who are you": ["I am a Python chatbot designed to help you.", "I'm just a simple script, but I try my best!"],
    "what are you doing": ["I'm chatting with you, of course!", "Just running some algorithms and enjoying our chat."],
    "how do you work": ["I use simple keyword matching and predefined rules to understand you.", "I look for patterns in what you say and respond accordingly."],
    "i am just bored": ["Let's find something fun to talk about! What are you interested in?", "I'm here to entertain you! Ask me anything!"],
    "i am bored": ["Boredom is just the brain asking for a new challenge. What are your hobbies?", "I can chat with you to pass the time!"],
    "im bored": ["Boredom is just the brain asking for a new challenge. What are your hobbies?", "I can chat with you to pass the time!"],
    "bored": ["If you are bored, I can tell you about how I work, or we can just chat!", "Let's cure that boredom! What do you like to do?"]
}

# Small talk
SMALL_TALK_KEYWORDS = ["how are you", "how are you doing", "what's up", "whats up"]
SMALL_TALK_RESPONSES = [
    "I'm just code, but I'm running perfectly! How about you?",
    "I'm doing well, ready to answer your questions!",
    "All systems nominal! How can I help?",
    "I'm feeling quite chatty today!"
]

# Fallbacks
FALLBACK_RESPONSES = [
    "I'm not sure I understand. Can you rephrase?",
    "That's interesting, but I don't know how to respond to that.",
    "Could you clarify what you mean?",
    "I'm still learning and didn't catch that. Could you try again?"
]
