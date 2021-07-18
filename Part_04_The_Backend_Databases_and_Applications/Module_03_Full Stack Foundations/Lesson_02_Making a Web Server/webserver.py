from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class WebserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith("/hello"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = ""
            message += "<html><body>Hello!</body></html>"
            self.wfile.write(message)
            print(message)
            return

        if self.path.endswith("/hola"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = ""
            message += "<html><body> &#161 Hola ! </body></html>"
            self.wfile.write(message)
            print message
            return
            
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)

def main():
    try:
        PORT = 8080
        server = HTTPServer(('', PORT), WebserverHandler)
        print("Server running running on port %s" % PORT)
        server.serve_forever()

    except KeyboardInterrupt:
        print("^C entered stopping server....")
        server.socket.close()

if __name__ == '__main__':
    main()