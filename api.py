from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 5000  # You can choose a different port if needed

class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Simulate back-end data (replace with your actual logic)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes("<h1>Tours Data</h1>", "utf-8"))

httpd = HTTPServer(('', PORT), SimpleRequestHandler)
print(f"Serving at http://localhost:{3306}")
httpd.serve_forever()
