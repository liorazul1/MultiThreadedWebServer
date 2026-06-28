# Return the MIME type based on file extension
def get_content_type(path):

    if path.endswith(".html"):
        return "text/html"

    if path.endswith(".css"):
        return "text/css"

    if path.endswith(".jpg"):
        return "image/jpeg"

    if path.endswith(".jpeg"):
        return "image/jpeg"

    if path.endswith(".png"):
        return "image/png"

    if path.endswith(".txt"):
        return "text/plain"

    # Use a generic binary type for unknown files
    return "application/octet-stream"