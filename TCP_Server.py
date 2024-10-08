import socket
import threading

IP = '0.0.0.0'
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f'[*] listening on {IP}:{PORT}')
    
    
    while True:
        client, address = server.accept()
        print(f'[*] Accepted connecton from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handleclient, args = (client,))
        client_handler.start()
    
    
def  handleclient(client_socket):
        with client_socket as socket:
            request = socket.recv(1024)
            print(f'[*] Received: {request.decode('UTF-8')}')
            
if __name__ == '__main__':
    main()
