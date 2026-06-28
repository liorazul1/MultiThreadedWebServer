# Extract request information from the HTTP request
def parse_request(request_text):

    lines = request_text.split("\r\n")

    if not lines or len(lines[0].split()) != 3:
        return None

    method, path, version = lines[0].split()

    # This server supports GET requests only
    if method != "GET":
        return None

    return {
        "method": method,
        "path": path,
        "version": version
    }