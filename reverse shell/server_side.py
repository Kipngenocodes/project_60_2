import socket


server_host = "0.0.0.0"
server_port = 5003
# 128kb is the max size of messages and relatively easy to increas based on your choice
buffer_size = 1024 *128

# separator string for sending two messages at a go
separator = "<sep>"

# socket creation 
s = socket.socket()

# binding socket to all the IP Addresses of this host
s.bind((server_host, server_port))