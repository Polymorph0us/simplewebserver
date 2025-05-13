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
