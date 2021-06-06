from requestHandler import CrawlerHTTPRequestHandler
from http.server import HTTPServer
import argparse

def main():
    parser = argparse.ArgumentParser(description="Distributed Web Crawler backend.")
    parser.add_argument('-p', help="Port for http api", default=8080, type=int)

    args=parser.parse_args()
    run(args.p)


def run(port):
    print("starting server at: {}".format(port))
 
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, CrawlerHTTPRequestHandler)
    print('running server...')
    httpd.serve_forever()

main()