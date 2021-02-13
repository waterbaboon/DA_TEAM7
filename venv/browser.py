# First HTTP Server
import socket

# HTTP Request
def handle_request(request):
    """Handles the HTTP request."""

    headers = request.split('\n')
    filename = headers[0].split()[1]
    if filename == '/':
        filename = '/index.html'

    try:
        fin = open('venv' + filename)
        content = fin.read()
        fin.close()

        response = 'HTTP/1.0 200 OK\n\nHello!' + content
    except FileNotFoundError:
        response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found..'

    return response

# Define the host as a tuple
HOST, PORT = "", 6969

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind((HOST,PORT))
s.listen(True)

print("Serving HTTP on port %s..." %PORT)

while True:
    client_connection, client_address = s.accept() # Wait for client connections

    request = client_connection.recv(1024).decode("utf-8") # Get client request, Buffer Size
    print(request) # Display the HTTP request

    response = handle_request(request)
    client_connection.sendall(response.encode())

    # client_connection.sendall(bytes(response.encode(),"utf-8"))
    client_connection.close()

s.close() # Close socket