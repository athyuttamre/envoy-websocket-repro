#!/usr/bin/env python3
import http.server
import socketserver


class AuthHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Force a minimal 401 Unauthorized with no body (Content-Length: 0)
        # (Or change to 200 if you prefer reproducing a successful response.)
        self.send_response(401, "Unauthorized")
        self.send_header("Content-Length", "0")
        self.end_headers()
        # No body sent.


def run_authz_server(port=9001):
    with socketserver.TCPServer(("", port), AuthHandler) as httpd:
        print(f"[authz] Listening on :{port}")
        httpd.serve_forever()


if __name__ == "__main__":
    run_authz_server()
