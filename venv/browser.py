# First HTTP Server
import socket
import http.server
import socketserver

# Define the host as a tuple
HOST, PORT = "", 6969

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Server started at localhost:" + str(PORT))
    httpd.serve_forever()


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


# Create an object of the above class
handler_object = MyHttpRequestHandler

my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
my_server.serve_forever()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(True)

print("Serving HTTP on port %s..." % PORT)

while True:
    conn, addr = s.accept()
    rqst = conn.recv(1024)  # Buffer Size
    print(rqst.decode("utf-8"))  # Display the HTTP request
    # Define the Web response message
    resp = 'HTTP/1.0 200 OK\n\nChing Chong Hon Chi'
    conn.sendall(bytes(resp, "utf-8"))
    conn.close()

# s.close()  # Closes socket
