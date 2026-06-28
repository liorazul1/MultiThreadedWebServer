# Multi-Threaded HTTP/1.0 Web Server

## Project Overview
This project implements a multi-threaded HTTP/1.0 web server from scratch using Python sockets.
The server accepts TCP client connections, parses HTTP requests, serves static files, detects MIME types, and generates appropriate HTTP responses. Multiple clients can be handled concurrently using threads.
The project was developed as part of the Computer Networks course.

## Gihub Link:
  https://github.com/maayaneshco/MultiThreadedWebServer

## Explanatory video:
  https://drive.google.com/file/d/1rPleQPe5IEPkItvjlPRYn-zy7T6ih1Fv/view?usp=sharing

## Technologies Used
- Python 3.14
- TCP Sockets
- HTTP/1.0
- Multi-Threading

## Features
- TCP socket communication
- HTTP request parsing
- HTTP/1.0 response generation
- Multi-threaded client handling
- Static file serving
- MIME type detection
- Directory traversal protection
- Support for HTML, CSS, TXT and image files
- Error handling with appropriate HTTP status codes

## Supported HTTP Status Codes
200 OK - Request completed successfully 
400 Bad Request - Invalid HTTP request   
403 Forbidden - Access to the requested resource is denied
404 Not Found -  Requested file does not exist
500 Internal Server Error - Unexpected server-side error  

## System Architecture
Browser --> request_reader.py --> request_parser.py --> file_handler.py --> mime_types.py 
 --> response_builder.py --> Browser

## Project Structure
MultiThreadedWebServer
│
├── server.py
│
├── handlers
│   ├── file_handler.py
│   ├── mime_types.py
│   ├── request_parser.py
│   ├── request_reader.py
│   └── response_builder.py
│
├── static
│   ├── css
│   │   └── style.css
│   │
│   ├── docs
│   │   └── info.txt
│   │
│   ├── images
│   │   └── cat.jpg
│   │
│   └── pages
│       ├── about.html
│       └── index.html
│
└── README.md

## File Responsibilities

* server.py
  The main server file responsible for:
   - Creating the TCP socket
   - Binding the server to an IP address and port
   - Listening for incoming connections
   - Creating a new thread for each client
   - Coordinating request processing and response generation

* request_reader.py
  Reads the HTTP request from the client socket until the end of the HTTP headers is reached.

* request_parser.py
  Parses the HTTP request and extracts:
   - HTTP Method
   - Requested Path
   - HTTP Version
   - The server supports GET requests only.

* file_handler.py
  Validates requested paths, prevents unauthorized access attempts, and reads files from the static directory.

* mime_types.py
  Determines the correct MIME type according to the requested file extension.

* response_builder.py
  Builds HTTP responses for successful requests and error conditions.

## Security Features
The server implements several security mechanisms:
- Directory traversal protection
- Access restriction to approved directories only
- Validation of incoming HTTP requests
- Stateless request handling

## Supported File Types
- HTML
- CSS
- TXT
- JPG
- JPEG
- PNG

## Running the Server
1. Open a terminal in the project directory.
2. Run the server: python server.py
3. Open a browser and navigate to: http://localhost:8080/pages/index.html
   Example Resources:
   - /pages/index.html
   - /pages/about.html
   - /css/style.css
   - /images/cat.jpg
   - /docs/info.txt

## Demo Video Link

## Group Members
Hadar Yakuti 212695183.
Maayan Eshco 207175761.
Lior Azoulay 212326466.
Computer Networks Course (863516901).
Bar-Ilan University, 2026.
