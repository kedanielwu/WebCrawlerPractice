from lxml import etree
from Program import *
from Finder import *


class ProgramFinder(Finder):

    def __init__(self, domain):
        Finder.__init__(self, domain)
        self.programs = {} # program: url 

        # Data Extraction
        self.data_extraction()

    # Getter

    def get_programs(self):
        return self.programs

    # Parent Class Implementation

    def data_extraction(self):
        html = self.request()
        tree = etree.HTML(html)
        tag = tree.xpath(u'//li/a')
        for program in tag:
            link = program.attrib["href"]
            if link.startswith("http"):
                url = link
                visible = False
            else:
                url = self.domain + link
                visible = True
            name = program.text.strip("\n\r\t' '")
            instance = Program(name, url, visible)
            self.programs[name] = instance

    def data_construction(self):
        return


