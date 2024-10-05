import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9999))

# Send some data
client.send(b"Hello, server!")

# Shut down the connection gracefully (disallow both sends and receives)
client.shutdown(socket.SHUT_RDWR)

# Close the socket
client.close()
