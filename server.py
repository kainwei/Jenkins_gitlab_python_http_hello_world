import http.server
import socketserver
import time
from http import HTTPStatus
import os
import socket


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b'Hello world10000')

var = 'true'
while var == 'true':
    try:
        httpd = socketserver.TCPServer(('', 8000), Handler)
        httpd.serve_forever()
        var = 'false'
    except:
        print("Waiting port down... ")
        time.sleep(1)
        



