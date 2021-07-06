from http.server import BaseHTTPRequestHandler
from db import *
import json

class CrawlerHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        print(self.path)
        if self.path.startswith("/pushUrls"):
            token = (self.path.split("&")[1]).split("=")[1]
            
            data = self.rfile.read(int(self.headers['Content-Length'])).decode()
            dataJson = json.loads(data)

            #todo check token
            writeUrls(dataJson["urls"], token)

        elif self.path.startswith("/register"):
            token = getToken()
            data = {"token" : token}

            #todo check token
            self.wfile.write(bytes(json.dumps(data), "utf8"))
        else:
            print("Else")
            self.wfile.write(bytes("Hello World!!", "utf8"))