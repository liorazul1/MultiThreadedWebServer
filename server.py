# Importing libraries
import socket
import threading

# Importing project functions
from handlers.request_reader import read_http_request
from handlers.request_parser import parse_request
from handlers.file_handler import get_file_content
from handlers.mime_types import get_content_type
from handlers.response_builder import (
    build_200_response,
    build_301_response,
    build_302_response,
    build_404_response,
    build_403_response,
    build_400_response,
    build_500_response
)

HOST = "127.0.0.1"
PORT = 8080


# Handle a single client connection
def handle_client(client_socket, client_address):

    print(f"\nConnection received from {client_address}")

    try:

        # Read the HTTP request from the client socket
        request_data = read_http_request(
            client_socket
        )

        # Convert bytes into readable text
        request_text = request_data.decode(
            "utf-8",
            errors="ignore"
        )

        # Extract method, path and HTTP version
        request_info = parse_request(
            request_text
        )

        if request_info is None:

            response = build_400_response()

        else:
            
            if request_info["path"] == "/redirect301":
                response = build_301_response("/pages/index.html")
            elif request_info["path"] == "/redirect302":
                response = build_302_response("/pages/index.html")
                
            else:

                # Locate and read the requested file
                file_content = get_file_content(
                    request_info["path"]
                )

                if file_content == "FORBIDDEN":

                    response = build_403_response()

                elif file_content is None:

                    response = build_404_response()

                else:

                    # Determine the correct MIME type
                    content_type_path = request_info["path"]
                    
                    if content_type_path == "/":
                        content_type_path = "/pages/index.html"
                        
                    content_type = get_content_type(
                        content_type_path
                    )

                    # Build a successful HTTP response
                    response = build_200_response(
                        file_content,
                        content_type
                    )

        # Send the HTTP response back to the client
        client_socket.sendall(response)

    except Exception as error:

        print(f"Error: {error}")

        # Return a server error response
        response = build_500_response()

        client_socket.sendall(response)

    finally:

        # Close the connection after handling the request
        client_socket.close()


# Create a TCP socket using IPv4
server_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

# Allow quick server restart after shutdown
server_socket.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_REUSEADDR,
    1
)

# Bind the server to the configured IP and port
server_socket.bind((HOST, PORT))

# Start listening for incoming connections
server_socket.listen(5)

print(f"Server is listening on {HOST}:{PORT}")

while True:

    # Wait for a new client connection
    client_socket, client_address = server_socket.accept()

    # Handle each client in a separate thread
    client_thread = threading.Thread(
        target=handle_client,
        args=(client_socket, client_address)
    )

    client_thread.start()