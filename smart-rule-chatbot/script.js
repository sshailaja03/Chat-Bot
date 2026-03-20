document.addEventListener('DOMContentLoaded', () => {
    const chatForm = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');
    const chatHistory = document.getElementById('chat-history');
    const typingIndicator = document.getElementById('typing-indicator');

    function formatTime(date) {
        return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    }

    function addMessage(content, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', sender);
        
        const contentDiv = document.createElement('div');
        contentDiv.classList.add('message-content');
        contentDiv.textContent = content;
        
        const timeDiv = document.createElement('div');
        timeDiv.classList.add('timestamp');
        timeDiv.textContent = formatTime(new Date());

        messageDiv.appendChild(contentDiv);
        messageDiv.appendChild(timeDiv);
        
        chatHistory.appendChild(messageDiv);
        scrollToBottom();
    }

    function scrollToBottom() {
        chatHistory.scrollTop = chatHistory.scrollHeight;
    }

    function showTyping() {
        typingIndicator.style.display = 'flex';
    }

    function hideTyping() {
        typingIndicator.style.display = 'none';
    }

    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const message = userInput.value.trim();
        if (!message) return;

        // Display user message
        addMessage(message, 'user');
        userInput.value = '';
        
        // Ensure bot is 'typing'
        showTyping();
        scrollToBottom();

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: message })
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            
            // Artificial delay to simulate processing & typing time
            setTimeout(() => {
                hideTyping();
                addMessage(data.response, 'bot');
            }, 800 + Math.random() * 500);

        } catch (error) {
            hideTyping();
            addMessage("Sorry, I'm having trouble connecting to my brain right now.", 'bot');
            console.error('Error:', error);
        }
    });

    // Initial focus
    userInput.focus();
    scrollToBottom();
});
