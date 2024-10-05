import socket

def get_http_response(host, port=80):
    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print(f"Connected to {host}:{port}")

    # send a GET request
    request = f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n"
    client.send(request.encode())

    # receive the response
    response = client.recv(4096)
    client.close()
    
    return response.decode()

# Initial request
target_host = "www.google.com"
response = get_http_response(target_host)

print(response)

# If redirected (301), follow the new location
if "301 Moved Permanently" in response:
    # Find the new location in the response headers
    new_location = response.split("Location: ")[1].split("\r\n")[0]
    print(f"Redirecting to {new_location}...")
    
    # Extract the new host (without the 'http://' part)
    new_host = new_location.split("://")[1].split("/")[0]
    new_response = get_http_response(new_host)
    
    print(new_response)
