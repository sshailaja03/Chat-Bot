"""
A built-in Python HTTP server to host the Chatbot Web UI and handle API requests.
"""
import http.server
import socketserver
import json
from urllib.parse import urlparse
from chatbot import SmartChatbot

PORT = 8000
bot = SmartChatbot()

class ChatHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Prevent caching of our API and dynamic files
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        super().end_headers()

    def do_GET(self):
        # Serve index.html by default
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

    def do_POST(self):
        # Handle the /chat API endpoint
        if self.path == '/chat':
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length > 0:
                try:
                    post_data = self.rfile.read(content_length)
                    data = json.loads(post_data.decode('utf-8'))
                    user_message = data.get('message', '')
                    
                    # Log message locally
                    bot.log_message("You", user_message)
                    
                    # Generate response
                    reply = bot.get_response(user_message)
                    bot.log_message(bot.bot_name, reply)
                    
                    # Send response back to UI
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    response = {'response': reply}
                    self.wfile.write(json.dumps(response).encode('utf-8'))
                    return
                except Exception as e:
                    self.send_response(500)
                    self.send_header('Content-Type', 'text/plain')
                    self.end_headers()
                    self.wfile.write(b'Internal Server Error')
                    print(f"Error handling request: {e}")
                    return

        # Return 404 for any other POST requests
        self.send_response(404)
        self.end_headers()

if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), ChatHTTPRequestHandler) as httpd:
        print(f"Starting server at http://localhost:{PORT}")
        print("Press Ctrl+C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")
