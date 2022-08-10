import socketserver
import http.server
import urllib.request
PORT = 9097
class MyProxy(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		url=self.path[1:]
		self.send_response(200)
		self.end_headers()
		url = 'http://192.168.1.253:8097'
		self.copyfile(urllib.request.urlopen(url), self.wfile)
httpd = socketserver.ForkingTCPServer(('', PORT), MyProxy)
print ("Now serving at "+str(PORT))
httpd.serve_forever()