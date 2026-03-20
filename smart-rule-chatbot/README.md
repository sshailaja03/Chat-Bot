# Smart Rule Chatbot

A clean, modular rule-based complete command-line chatbot built with pure Python. 
The chatbot can interact with users using predefined rules and pattern matching. It does not use any heavy external AI APIs and is completely lightweight.

## Features

- **Greeting Detection:** Recognizes different ways of saying hello and dynamically responds.
- **Question Handling:** Parses common questions and provides intelligent predefined responses.
- **Small Talk:** Can engage in basic chit-chat like "how are you," "who are you," etc.
- **Fallback Response:** Gracefully falls back if it doesn't understand the user's input.
- **Exit Gracefully:** Typing 'exit', 'bye', or 'quit' will end the session.
- **Typing Effect:** Responses use a slight delay mimicking a real human typing.
- **Timestamps & Chat History:** Displays timestamps for messages and outputs the chat history when exiting.
- **Clean Input:** Handles case differences, extra spaces, and basic punctuation gracefully.

## Project Structure

- `chatbot.py`: Main bot application containing the core loop and logic structure.
- `utils.py`: Reusable utility functions for cleaning input and UI effects (typing simulation, timestamps).
- `responses.py`: Single source of truth for pattern-to-response definitions.

## Requirements
- Python 3.6 or higher.
- No external dependencies needed. 

## How to Run

Navigate to the project directory and run:

```bash
python chatbot.py
```

## Example Conversation

```text
========================================
Welcome to the SmartBot interface!
Type 'exit' or 'bye' to end the chat.
========================================

[02:15 PM] SmartBot: Hello! I am ready to chat. How can I help you today?

You: hello
[02:15 PM] SmartBot: Hi there! How can I help you today?

You: what is your name
[02:15 PM] SmartBot: I am SmartBot, your friendly assistant.

You: how are you
[02:15 PM] SmartBot: I'm just code, but I'm running perfectly! How about you?

You: can we talk about quantum physics?
[02:16 PM] SmartBot: I'm not sure I understand. Can you rephrase?

You: exit
[02:16 PM] SmartBot: Goodbye! Have a great day!

--- Chat History with SmartBot ---
[02:15 PM] SmartBot: Hello! I am ready to chat. How can I help you today?
[02:15 PM] You: hello
[02:15 PM] SmartBot: Hi there! How can I help you today?
[02:15 PM] You: what is your name
[02:15 PM] SmartBot: I am SmartBot, your friendly assistant.
[02:15 PM] You: how are you
[02:15 PM] SmartBot: I'm just code, but I'm running perfectly! How about you?
[02:16 PM] You: can we talk about quantum physics?
[02:16 PM] SmartBot: I'm not sure I understand. Can you rephrase?
[02:16 PM] You: exit
[02:16 PM] SmartBot: Goodbye! Have a great day!
---------------------------------
```
