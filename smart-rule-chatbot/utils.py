"""
Helper functions for the chatbot, providing utility features like text cleaning,
typing effects, and timestamp generation.
"""

import time
import sys
from datetime import datetime
import re

def clean_input(user_input):
    """
    Cleans the user input by converting it to lowercase and removing extra spaces.
    
    Args:
        user_input (str): The raw input from the user.
        
    Returns:
        str: The cleaned and normalized input string.
    """
    if not user_input:
        return ""
    # Convert to lowercase
    cleaned = user_input.lower()
    # Remove extra spaces replacing multiple whitespace characters with a single space
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    # Remove basic punctuation for easier matching (optional, keeping it simple)
    cleaned = re.sub(r'[^\w\s]', '', cleaned)
    return cleaned

def print_with_typing_effect(text, delay=0.03):
    """
    Simulates a typing effect by printing text character by character with a small delay.
    
    Args:
        text (str): The text to print.
        delay (float): The delay between printing each character in seconds.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() # Print a newline at the end

def get_timestamp():
    """
    Gets the current time formatted as a string.
    
    Returns:
        str: The formatted time string (e.g., '10:30 AM').
    """
    now = datetime.now()
    return now.strftime("%I:%M %p")
