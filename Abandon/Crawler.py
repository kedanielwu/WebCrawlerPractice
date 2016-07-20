import urllib
import urllib2
from lxml import etree
from Course import *
from UTAnalysis import *

class Crawler:

    # 2016/07/12 Crawler class is no longer used
    # Replaced by Finder/CourseFinder class

    def __init__(self, domain):
        # main domain is
        # http://www.artsandscience.utoronto.ca/ofr/timetable/winter/csc.html
        # info page domain is 
        # http://coursefinder.utoronto.ca/course-search/search/courseInquiry?methodToCall=start&viewId=CourseDetails-InquiryView&courseId=
        self.info = "http://coursefinder.utoronto.ca/course-search/search/courseInquiry?methodToCall=start&viewId=CourseDetails-InquiryView&courseId="
        self.domain = domain
        self.course_set = set()
        self.courses = {}
        self.term = {'F': 'F', 'S': 'S', 'Y': 'Y'}
        self.year = {'F': "20169", 'S':"20171"}

        # Data Extraction
        self.extract_course_code()
        self.course_init()

    # Getters

    def get_courses(self):
        return self.courses

    # Setters

    # Methods

    def request(self, url):
        '''
        return the html of the page
        '''
        page = urllib2.urlopen(url)
        html = page.read()
        return html

    # UT specific
    def add_course(self, course_code):
        self.course_set.add(course_code)

    # UT specific
    def extract_course_code(self):
        html = etree.HTML(self.request(self.domain))
        content = html.xpath(u'//td//a')
        for course in content:
            if course.attrib["href"].startswith("http"):
                tag = course.text
            ## Testing Code
            #if tag.startswith('CSC2'):
                self.add_course(tag)
    
    # UT specific
    def course_init(self):
        for course in self.course_set:
            instance = Course(course, self.term, self.year)
            url = self.info + course + self.term['F'] + self.year['F']
            html = self.request(url)
            instance.set_info_page(html)
            self.courses[course] = instance
        UTAnalysis(self.get_courses())

    

        
        
            



    
        
