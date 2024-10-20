import socket

# Target host and port
target_host = "127.0.0.1"
target_port = 9998

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
try:
    client.connect((target_host, target_port))
    print(f"Connected to {target_host}:{target_port}")

    # Send some data (HTTP request)
    request = f"GET / HTTP/1.1\r\nHost: {target_host}\r\nConnection: close\r\n\r\n"
    client.send(request.encode())

    # Receive some data
    response = b""
    while True:
        data = client.recv(4096)
        if not data:
            break
        response += data

    print(response.decode())
finally:
    # Closing the client
    client.close()
