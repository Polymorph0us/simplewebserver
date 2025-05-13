# EX01 Developing a Simple Webserver
## Name : Keerthan D
## Reg no. : 212224240075
## Date: 18.04.2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                color: #333;
                text-align: center;
            }
            h1 {
                color: #4CAF50;
                margin-top: 20px;
            }
            ul {
                list-style-type: none;
                padding: 0;
            }
            li {
                margin: 10px 0;
                font-size: 18px;
                background-color: #fff;
                padding: 10px;
                border-radius: 5px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            }
        </style>
    </head>
    <body>
        <h1>DEVICE CONFIGURATION - POLYMORPHOUS</h1>
        <ul>
            <li><b>Device name:</b> Polymorphous</li>
            <li><b>Processor:</b> Intel(R) Core(TM) i5-1234U 1.80 GHz</li>
            <li><b>Installed RAM:</b> 16.0 GB (15.7 GB usable)</li>
            <li><b>Device ID:</b> 12345678-ABCD-EFGH-IJKL-9876543210MN</li>
            <li><b>Product ID:</b> 98765-43210-12345-XYZABC</li>
            <li><b>System type:</b> 64-bit operating system, x64-based processor</li>
            <li><b>Pen and touch:</b> No pen or touch input is available for this display</li>
        </ul>
    </body>
</html>
"""

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request received")
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('', 8000)
httpd = HTTPServer(server_address, MyHandler)
print("My webserver is running...")
httpd.serve_forever()
```

## OUTPUT:
![alt text](<Screenshot 2025-05-13 111441.png>)

![alt text](<Screenshot 2025-05-13 111516.png>)
## RESULT:
The program for implementing simple webserver is executed successfully.
