import socket

# Define the server address and port
server_host = '127.0.0.1'
server_port = 9997

# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address and port
server.bind((server_host, server_port))
print(f"Server listening on {server_host}:{server_port}")

try:
    while True:
        # Receive data from the client
        data, addr = server.recvfrom(4096)
        print(f"Received message: {data.decode()} from {addr}")

        # Send a response back to the client
        server.sendto(b'Hello from server!', addr)
except KeyboardInterrupt:
    print("\nServer is shutting down...")
finally:
    server.close()
