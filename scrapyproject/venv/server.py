import http.server
import socketserver

PORT = 6969
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as http:
    print("Hosting via Port:", PORT)
    http.serve_forever()
