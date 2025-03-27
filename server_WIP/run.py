import http.server
import socketserver
import webbrowser
import threading
import time
import os

PORT = 8000
STOP_SERVER = False

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        return  # Disable logging

    def do_GET(self):
        if self.path == "/shutdown":
            global STOP_SERVER
            STOP_SERVER = True
            self.send_response(200)
            self.end_headers()
            return
        super().do_GET()

# Start the server in a separate thread
def start_server():
    global STOP_SERVER
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Serving at http://localhost:{PORT}/homePage.html")
        
        while not STOP_SERVER:  # Keep server running unless STOP_SERVER is set to True
            httpd.handle_request()

        print("Server shutting down...")
        os._exit(0)

# Open the webpage in a browser
def open_browser():
    time.sleep(1)  # Delay to ensure server starts first
    webbrowser.open(f"http://localhost:{PORT}/homePage.html")

# Run both the server and browser
server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()

open_browser()
