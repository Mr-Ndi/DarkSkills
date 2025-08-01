import http.server
import webbrowser
import requests
import threading
import urllib.parse
import os

# === CONFIG ===
CLIENT_ID = "2b10fd65-f60e-4e31-a3ac-3e9d4092f8d4"  # ← from your integration
REDIRECT_URI = "http://localhost:8765/callback"
SCOPES = "data.records:read data.records:write"
AUTH_URL = "https://airtable.com/oauth2/v1/authorize"
TOKEN_URL = "https://airtable.com/oauth2/v1/token"

# === Local server to catch OAuth callback ===
auth_code = None

class OAuthHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        global auth_code
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        if "code" in params:
            auth_code = params["code"][0]
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Authorization successful. You can close this tab.")
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Authorization failed.")

def run_server():
    server = http.server.HTTPServer(("localhost", 8765), OAuthHandler)
    server.handle_request()

# === Step 1: Open browser to login ===
params = {
    "response_type": "code",
    "client_id": CLIENT_ID,
    "redirect_uri": REDIRECT_URI,
    "scope": SCOPES,
}
url = f"{AUTH_URL}?{urllib.parse.urlencode(params)}"
print(f"🌐 Opening browser for auth: {url}")
threading.Thread(target=run_server).start()
webbrowser.open(url)

# === Step 2: Wait for auth code ===
while not auth_code:
    pass

print(f"🔑 Received auth code: {auth_code}")

# === Step 3: Exchange code for access token ===
data = {
    "grant_type": "authorization_code",
    "code": auth_code,
    "client_id": CLIENT_ID,
    "redirect_uri": REDIRECT_URI,
}
response = requests.post(TOKEN_URL, data=data)

if response.ok:
    tokens = response.json()
    print("✅ Access token:", tokens["access_token"])
    # Optionally save to .env or file
else:
    print("❌ Failed to fetch token:", response.text)
