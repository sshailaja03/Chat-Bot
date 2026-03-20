"""
Main logic for the Smart Rule Chatbot.
Handles the main loop, input processing, response generation, and history tracking.
"""

import sys
import random
from utils import clean_input, print_with_typing_effect, get_timestamp
import responses

class SmartChatbot:
    def __init__(self):
        """Initialize the chatbot and its conversation history."""
        self.bot_name = "SmartBot"
        self.history = []

    def log_message(self, sender, message):
        """Log a message to the chat history."""
        timestamp = get_timestamp()
        entry = f"[{timestamp}] {sender}: {message}"
        self.history.append(entry)
        return timestamp
        
    def respond(self, message, timestamp):
        """Prints the bot's response with a typing effect."""
        output = f"[{timestamp}] {self.bot_name}: "
        sys.stdout.write(output)
        sys.stdout.flush()
        print_with_typing_effect(message)

    def detect_greeting(self, text):
        """Check if the text contains any greeting keywords."""
        words = text.split()
        for word in words:
            if word in responses.GREETINGS_KEYWORDS:
                return random.choice(responses.GREETINGS_RESPONSES)
        
        # Check for multi-word greetings
        for kw in responses.GREETINGS_KEYWORDS:
            if kw in text:
                return random.choice(responses.GREETINGS_RESPONSES)
                
        return None

    def handle_specific_question(self, text):
        """Check if the text matches any specific questions exactly or loosely."""
        for question, replies in responses.QUESTIONS_SPECIFIC.items():
            if clean_input(question) in text:
                return random.choice(replies)
        return None

    def handle_smalltalk(self, text):
        """Check if the text matches small talk."""
        for phrase in responses.SMALL_TALK_KEYWORDS:
            if phrase in text:
                return random.choice(responses.SMALL_TALK_RESPONSES)
        return None

    def get_response(self, user_input):
        """Determine the best response based on the input text."""
        cleaned_input = clean_input(user_input)
        
        if not cleaned_input:
            return "Please say something!"

        # 1. Check for specific small talk
        small_talk_reply = self.handle_smalltalk(cleaned_input)
        if small_talk_reply:
            return small_talk_reply

        # 2. Check for specific known questions
        question_reply = self.handle_specific_question(cleaned_input)
        if question_reply:
            return question_reply

        # 3. Check for greetings
        greeting_reply = self.detect_greeting(cleaned_input)
        if greeting_reply:
            return greeting_reply

        # 4. Fallback if no patterns matched
        return random.choice(responses.FALLBACK_RESPONSES)

    def print_history(self):
        """Print the complete conversation history."""
        print(f"\n--- Chat History with {self.bot_name} ---")
        for entry in self.history:
            print(entry)
        print("---------------------------------")

    def run(self):
        """Run the main chat loop."""
        print("========================================")
        print(f"Welcome to the {self.bot_name} interface!")
        print("Type 'exit' or 'bye' to end the chat.")
        print("========================================\n")
        
        # Initial greeting from bot
        init_msg = "Hello! I am ready to chat. How can I help you today?"
        ts = self.log_message(self.bot_name, init_msg)
        self.respond(init_msg, ts)

        while True:
            try:
                # Get raw user input
                user_text = input("\nYou: ")
                cleaned = clean_input(user_text)
                
                # Log user message
                self.log_message("You", user_text)
                
                # Check for exit command
                if cleaned in ["exit", "bye", "quit"]:
                    reply = "Goodbye! Have a great day!"
                    ts = self.log_message(self.bot_name, reply)
                    self.respond(reply, ts)
                    break
                    
                # Get generated response
                reply = self.get_response(user_text)
                
                # Log and print response
                ts = self.log_message(self.bot_name, reply)
                self.respond(reply, ts)
                
            except KeyboardInterrupt:
                # Handle Ctrl+C gracefully
                print("\n")
                self.respond("Goodbye! Have a great day!", get_timestamp())
                break
            except EOFError:
                # Handle Ctrl+D gracefully
                print("\n")
                self.respond("Goodbye! Have a great day!", get_timestamp())
                break

        # Optionally print history at the end
        self.print_history()

if __name__ == "__main__":
    bot = SmartChatbot()
    bot.run()
