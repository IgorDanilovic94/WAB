from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
student_dict = {'12':['Milkica', 'Dragic', '8.6'],'45':['Slavisa', 'Lukac', '6.7'],'34':['Vladan', 'Lulic', '7.8'],'14':['Milan', 'Tesanovic', '8.1']}
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.log_message("Incoming GET request...")
        try:
            indeks = parse_qs(self.path[2:])['indeks'][0]
        except:
            self.send_response_to_client(404, 'Incorrect parameters provided')
            self.log_message("Incorrect parameters provided")
            return

        if indeks in student_dict.keys():
            self.send_response_to_client(200, student_dict[indeks])
        else:
            self.send_response_to_client(400, 'Indeks nije pronadjen')
            self.log_message("Indeks nije pronadjen")

    def do_POST(self):
        self.log_message('Incoming POST request...')
        data = parse_qs(self.path[2:])
        try:
            student_dict[data['indeks'][0]] = [data['ime'][0], data['prezime'][0], data['prosjek'][0]]
            self.send_response_to_client(200, student_dict)
        except KeyError:
            self.send_response_to_client(404, 'Incorrect parameters provided')
            self.log_message("Incorrect parameters provided")
             
    def send_response_to_client(self, status_code, data):
        # Send OK status
        self.send_response(status_code)
        # Send headers
        self.send_header('Content-type', 'text/plain')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
     
        # Send the response
        self.wfile.write(str(data).encode())
 
server_address = ('127.0.0.1', 8080)
http_server = HTTPServer(server_address, RequestHandler)
http_server.serve_forever()

