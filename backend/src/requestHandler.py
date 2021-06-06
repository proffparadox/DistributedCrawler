from http.server import BaseHTTPRequestHandler

class CrawlerHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        self.wfile.write(bytes("Hello World!!!", "utf8"))