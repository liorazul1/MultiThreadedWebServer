# Build a 200 response
def build_200_response(file_content, content_type):

    # Create HTTP headers for the response
    headers = (
        "HTTP/1.0 200 OK\r\n"
        f"Content-Type: {content_type}\r\n"
        f"Content-Length: {len(file_content)}\r\n"
        "\r\n"
    )

    return headers.encode() + file_content


# Build a 404 response
def build_404_response():
    
    body = """
    <html>
        <body>
            <h1>404 Not Found</h1>
        </body>
    </html>
    """

    body_bytes = body.encode()

    headers = (
        "HTTP/1.0 404 Not Found\r\n"
        "Content-Type: text/html\r\n"
        f"Content-Length: {len(body_bytes)}\r\n"
        "\r\n"
    )

    return headers.encode() + body_bytes


# Build a 403 response
def build_403_response():

    body = """
    <html>
        <body>
            <h1>403 Forbidden</h1>
        </body>
    </html>
    """

    body_bytes = body.encode()

    headers = (
        "HTTP/1.0 403 Forbidden\r\n"
        "Content-Type: text/html\r\n"
        f"Content-Length: {len(body_bytes)}\r\n"
        "\r\n"
    )

    return headers.encode() + body_bytes


# Build a 400 response
def build_400_response():

    body = """
    <html>
        <body>
            <h1>400 Bad Request</h1>
        </body>
    </html>
    """

    body_bytes = body.encode()

    headers = (
        "HTTP/1.0 400 Bad Request\r\n"
        "Content-Type: text/html\r\n"
        f"Content-Length: {len(body_bytes)}\r\n"
        "\r\n"
    )

    return headers.encode() + body_bytes


# Build a 500 response
def build_500_response():

    body = """
    <html>
        <body>
            <h1>500 Internal Server Error</h1>
        </body>
    </html>
    """

    body_bytes = body.encode()

    headers = (
        "HTTP/1.0 500 Internal Server Error\r\n"
        "Content-Type: text/html\r\n"
        f"Content-Length: {len(body_bytes)}\r\n"
        "\r\n"
    )

    return headers.encode() + body_bytes