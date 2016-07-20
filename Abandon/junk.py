import urllib

from lxml import etree
from WebCapture import *
from WebAnalysis import *
from FileSystem import *
from Crawler import *
from Course import *
from ProgramFinder import *

# WebCapture is no longer used 2017/07/11

def setup():
    crawler = WebCapture('F', 'CSC', 2016, 'H', 100)
    crawler.address_construct()
    crawler.request_url()
    cache = crawler.get_cache()
    result = WebAnalysis(cache)
    return result

def main():
    program_finder = ProgramFinder()
    programs = program_finder.get

def test():
    c = Crawler("http://www.artsandscience.utoronto.ca/ofr/timetable/winter/csc.html")
    c.extract_course_code()
    c.course_init()
    file = FileSystem("course.txt", c.get_courses())
    file.writing()
    print "finished"

def program():
    a = ProgramFinder()
    a.request
    a.extract_program()
    file = FileSystem("program.txt", a.get_programs())
    file.writing()
    print "finished"

if __name__ == "__main__":
    program()
    


