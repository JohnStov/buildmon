from httplib import HTTPConnection
from urlparse import urlparse, urlunparse
import json

class Connection:
    def __init__(self, url):

        port = 80
        parsed = urlparse(url)
        if parsed.port != None:
            port = parsed.port

        self.connection = HTTPConnection(parsed.hostname, port)

    def get_href(self, href, headers = {}):
        self.connection.request('GET', href, None, headers)
        response = self.connection.getresponse()
        if response.status == 200:
            return response.read().decode()
        else: 
            return None

    def get_href_json(self, href):
            value = self.get_href(href, { b"Accept" : b"application/json" })
            if value != None:
                value = json.loads(value) 
            return value

