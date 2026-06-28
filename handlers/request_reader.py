# Read the complete HTTP request from the client
def read_http_request(client_socket):

    data = b""

    while b"\r\n\r\n" not in data:

        chunk = client_socket.recv(1024)

        if not chunk:
            break

        data += chunk

    return data