# Smart Rule Chatbot

A lightweight rule-based chatbot with both a Python command-line interface and a browser UI served by Python's built-in HTTP server.

The implementation lives in [`smart-rule-chatbot/`](./smart-rule-chatbot/).

## Highlights

- Pattern-based greeting, question, and small-talk detection
- Randomised responses and fallback handling
- Conversation timestamps and session history
- Responsive HTML/CSS/JavaScript chat interface
- Dependency-free Python HTTP endpoint at `POST /chat`

## Run the command-line version

```bash
git clone https://github.com/sshailaja03/Chat-Bot.git
cd Chat-Bot/smart-rule-chatbot
python chatbot.py
```

## Run the web version

```bash
cd Chat-Bot/smart-rule-chatbot
python server.py
```

Open [http://localhost:8000](http://localhost:8000).

## Scope

This project uses deterministic rules and keyword matching; it is not a machine-learning or generative-AI system. Its purpose is to demonstrate modular Python, request handling, DOM updates, and graceful fallback behaviour.
