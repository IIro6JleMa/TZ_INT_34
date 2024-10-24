from http.server import BaseHTTPRequestHandler, HTTPServer

# sdelal obrabotchik zaprosov
class HealthCheckHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        # proverka /healtz
        if self.path == '/healthz':
            # kot otveta
            self.send_response(200)
            # zagolovok content-type v vide text/plain
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            # otvet na zapros OK
            self.wfile.write(b"200 OK")
        else:
            # if zapros ne sovpadaet to 404
            self.send_response(404)
            self.end_headers()

# Start servera
def run(server_class=HTTPServer, handler_class=HealthCheckHandler, port=8080):
# Infa po adressy and port servera(beretsa iz docker-compose.yml)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')  # vivod infi pri starte servera
    httpd.serve_forever()  # beskonechniy cikl zaprosov

if __name__ == '__main__':
    # start servera
    run()
