import os

ALLOWED_DIRECTORIES = [
    "pages",
    "css",
    "docs",
    "images"
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Validate the requested path and read the requested file
def get_file_content(path):

    # Block directory traversal attempts
    if ".." in path:
        return "FORBIDDEN"
    
    if path == "/":
        path = "/pages/index.html"

    relative_path = path.lstrip("/")

    path_parts = relative_path.split("/")

    requested_directory = path_parts[0]

    # Allow access only to approved directories
    if requested_directory not in ALLOWED_DIRECTORIES:
        return "FORBIDDEN"

    file_path = os.path.join(
        STATIC_ROOT,
        relative_path
        )

    # Return None if the requested file does not exist
    if not os.path.isfile(file_path):
        return None

    # Read the file content as bytes
    with open(file_path, "rb") as file:
        return file.read()