from Finder import *
from Course import *
from UTAnalysis import *


class CourseCodeException(Exception):
    # Code list
    # 100 - wrong term

    def __init__(self, code):
        Exception.__init__(self)
        self.error_code = code
        self.msg = ""
        if self.error_code == 100:
            self.msg = "Wrong Term Code"

    def __str__(self):
        return "CourseCodeException: " + self.msg


class CourseFinder(Finder):
    """
    this class extracts course code from timetable, and initiate
    the Course object for other class to storing information
    """

    def __init__(self, domain, term):
        Finder.__init__(self, domain)
        self.term = term
        self.year = '20169'
        try:
            if self.term == 'F':
                self.year = '20169'
            elif self.term == 'S':
                self.year = '20171'
            else:
                raise CourseCodeException(100)
        except CourseCodeException, e:
            print e
            exit(1)

        self.courses = {}
        self.info = "http://coursefinder.utoronto.ca/course-search/search/courseInquiry?methodToCall=start&viewId=CourseDetails-InquiryView&courseId="

        # setup
        self.data_extraction()
        self.data_construction()

    # Getter

    def get_courses(self):
        return self.courses

    # Register

    def add_course(self, coursecode):
        instance = Course(coursecode, self.term, self.year)
        self.courses[coursecode] = instance
        print "Course registered: ", coursecode

    # Parent Class Implementation

    def data_extraction(self):
        html = etree.HTML(self.request())
        content = html.xpath(u'//td//a')
        for course in content:
            if course.attrib["href"].startswith("http"):
                key = course.text
                # UT course code is length of 8
                if key not in self.courses and len(key) == 8:
                    self.add_course(key)

    def data_construction(self):
        for course in self.courses:
            term_code = self.term
            if course[6] == "Y":
                term_code = "Y"
            url = self.info + course + term_code + self.year
            html = urllib2.urlopen(url).read()
            self.courses[course].set_info_page(html)
            print "Course loaded: ", course
        UTAnalysis(self.get_courses())
