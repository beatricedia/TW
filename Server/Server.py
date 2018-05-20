import http.server
import socketserver
import os
import cgitb

port = 8001
ip = 'localhost'

cgitb.enable()
Handler = http.server.CGIHTTPRequestHandler

os.chdir(os.path.join(os.path.dirname(__file__),'..','MVC',))
with socketserver.TCPServer((ip, port), Handler) as httpd:
    print("serving at port", port)
    httpd.server_name = "test"
    httpd.server_port = port
    httpd.serve_forever()