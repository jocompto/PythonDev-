import http
from http.server import HTTPServer 
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse

class EchoHandler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        if (self.path.startswith('/test')):
            print( 'Web server called with path ' + self.path)
            #
            # self.wfile.write('''
            # <html><head>
            # <meta charset="UTF-8">
            # <title>Your Request</title>
            #</head>
            #<body>
            #<pre>
            #You requested the following: %s
            #Your request headers were:
            #%s
            #</pre></body></html>
            #''' % (self.path, self.headers))
            #
        if (self.path.startswith('/page')):
            print( 'Web server called with path ' + self.path)
           # fileHandle = open('page.html')
           # fileContent = fileHandle.read()
           # self.wfile.write(fileContent)
        if (self.path.startswith('/data')):
            print( 'Web server called with path ' + self.path)
            # self.wfile.write('This data comes from the web server!')
        
port = 8080
print('Listening on localhost:%s' % port) 

httpd = HTTPServer(('', port), EchoHandler)
httpd.serve_forever()