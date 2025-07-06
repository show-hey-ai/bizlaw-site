import webbrowser
import subprocess
import time
import os

# Change to script directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("Starting Bizlaw Site Server...")
print("Current directory:", os.getcwd())
print()

# Start server in background
server_process = subprocess.Popen(
    ["python", "-m", "http.server", "8080"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

print("Server starting on port 8080...")
time.sleep(2)

# Open browser
url = "http://localhost:8080"
print(f"Opening {url} in browser...")
webbrowser.open(url)

print()
print("Server is running!")
print("Press Ctrl+C to stop the server")
print()

try:
    # Keep the server running
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopping server...")
    server_process.terminate()
    print("Server stopped.")
