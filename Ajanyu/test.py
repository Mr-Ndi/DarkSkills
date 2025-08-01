import http.server
import socketserver
import urllib.parse
import requests
import secrets
import os

CLIENT_ID = os.getenv("AIRTABLE_CLIENT_ID")
CLIENT_SECRET = os.getenv("AIRTABLE_CLIENT_SECRET")
REDIRECT_URI = "http://localhost:8080/callback"
SCOPES = "data.records:read"  # adjust scopes as needed

STATE = secrets.token_urlsafe(16)

PORT = 8080

class OAuthHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        if parsed_path.path != "/callback":
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not found")
            return

        params = urllib.parse.parse_qs(parsed_path.query)
        if "error" in params:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(f"Error: {params['error'][0]}".encode())
            return

        # Validate state
        if "state" not in params or params["state"][0] != STATE:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid state. Potential CSRF attack.")
            return

        if "code" in params:
            code = params["code"][0]

            # Exchange code for access token
            token_url = "https://airtable.com/oauth2/v1/token"
            data = {
                "grant_type": "authorization_code",
                "code": code,
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "redirect_uri": REDIRECT_URI,
            }
            response = requests.post(token_url, data=data)
            if response.status_code != 200:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(f"Failed to get token: {response.text}".encode())
                return

            token_data = response.json()
            access_token = token_data.get("access_token")

            # Save or print access token
            print("\n✅ OAuth Access Token:")
            print(access_token)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Authentication successful! You can close this window.")

            # Optionally write token to .env or file here
            with open(".env", "a") as f:
                f.write(f"\nOAUTH_ACCESS_TOKEN={access_token}\n")

            # Stop server after success
            print("Stopping server...")
            def stop_server():
                httpd.shutdown()
            import threading
            threading.Thread(target=stop_server).start()
            return

        self.send_response(400)
        self.end_headers()
        self.wfile.write(b"Missing code parameter.")

def build_auth_url():
    base_auth_url = "https://airtable.com/oauth2/v1/authorize"
    params = {
        "response_type": "code",
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPES,
        "state": STATE
    }
    url = base_auth_url + "?" + urllib.parse.urlencode(params)
    return url

if __name__ == "__main__":
    print("Open this URL in your browser to authorize:")
    print(build_auth_url())

    with socketserver.TCPServer(("", PORT), OAuthHandler) as httpd:
        print(f"Serving at port {PORT}...")
        httpd.serve_forever()
