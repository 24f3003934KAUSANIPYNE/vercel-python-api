from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse_qs(self.path[6:])  # remove "/api?" part
        names = query.get("name", [])
        name_to_mark = {"X": 10, "Y": 20, "Z": 30}
        marks = [name_to_mark.get(name, 0) for name in names]

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")  # Enable CORS
        self.end_headers()
        self.wfile.write(bytes(f'{{"marks": {marks}}}', "utf-8"))
