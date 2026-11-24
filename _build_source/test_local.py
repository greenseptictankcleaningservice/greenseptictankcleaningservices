import http.server
import socketserver
import threading
import urllib.request
import time

PORT = 8999

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass # suppress logs

def run_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()
time.sleep(1)

test_urls = [
    f"http://localhost:{PORT}/index.html",
    f"http://localhost:{PORT}/services.html",
    f"http://localhost:{PORT}/about.html",
    f"http://localhost:{PORT}/areas.html",
    f"http://localhost:{PORT}/contact.html",
    f"http://localhost:{PORT}/css/style.css",
    f"http://localhost:{PORT}/js/script.js",
    f"http://localhost:{PORT}/images/logo.webp",
    f"http://localhost:{PORT}/images/main-slider/fast-efficient-septic-services.webp",
    f"http://localhost:{PORT}/images/resource/residential-septic-tank.webp"
]

all_passed = True
for u in test_urls:
    try:
        resp = urllib.request.urlopen(u, timeout=3)
        code = resp.getcode()
        size = len(resp.read())
        print(f"PASS [{code}] {u} -> {size} bytes")
    except Exception as e:
        print(f"FAIL {u} -> {e}")
        all_passed = False

if all_passed:
    print("\nALL URLS AND ASSETS VERIFIED SUCCESSFULLY 100%!")
else:
    print("\nSOME ASSETS FAILED!")
