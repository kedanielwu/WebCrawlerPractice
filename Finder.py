import urllib2

class Finder:

    def __init__(self, domain):
        self.domain = domain

    def request(self):
        page = urllib2.urlopen(self.domain)
        html = page.read()
        return html
    
    def data_extraction(self):
        raise NotImplementedError("Implemented in a subclass")

    def data_construction(self):
        raise NotImplementedError("Implemented in a subclass")
