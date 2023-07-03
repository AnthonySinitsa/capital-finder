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
    
    country = dic['country']
    url = "https://restcountries.com/v3.1/name/"
    response = requests.get(url + country)
    data = response.json()
    capital = data[0]['capital'][0]
    message = str(f'The capital of {country} is {capital}')
    #q: what is line 20 doing?
    #a: it is getting the capital of the country that the user inputted
    
    
    # definitions = []
    # for word_data in data:
    #   definition = word_data['meanings'][0]['definitions'][0]['definition']
    #   definitions.append(definition)
    
    message = str(message)
    self.wfile.write(message.encode())
    return
