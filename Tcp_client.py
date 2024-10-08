import socket 

target_host = "http://www.google.com/"
target_port = 80

# create a socket object 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))
print(f"connected  to {target_host}:{target_port}")


# send some data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
# receive some data
data = client.recv(4096)

print(data.decode())
# closing the client 
client.close()