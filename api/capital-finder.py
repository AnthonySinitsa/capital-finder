from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    path = self.path
    url_components = parse.urlsplit(path)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)
    
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    
    word = dic['word']
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
    response = requests.get(url + word)
    data = response.json()
    definitions = []
    for word_data in data:
      definition = word_data['meanings'][0]['definitions'][0]['definition']
      definitions.append(definition)
    
    message = str(definitions)
    self.wfile.write(message.encode())
    return
