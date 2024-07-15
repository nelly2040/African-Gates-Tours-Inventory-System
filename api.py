from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 5000  # You can choose a different port if needed

class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes("<h1>African Gates Tours</h1>", "utf-8"))
        elif self.path == '/about':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes("<h1>About Us</h1><p>We offer amazing tours!</p>", "utf-8"))
        else:
            self.send_error(404, "Page Not Found")

httpd = HTTPServer(('', PORT), SimpleRequestHandler)
print(f"Serving at http://localhost:{3306}")
httpd.serve_forever()
