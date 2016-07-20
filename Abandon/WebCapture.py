import urllib
import urllib2


class WebCapture:

    def __init__(self, term, program, year, credit, level=0):
        # format needs change
        # course code format: Program + code + credit + campus + term + year + season
        # example           : CSC       108    H        1        F      2016   9
        self.domain = "http://coursefinder.utoronto.ca/course-search/search/courseInquiry?methodToCall=start&viewId=CourseDetails-InquiryView&courseId="
        self.address_book = {}  # course_code: url
        self.page_cache = {}  # course_code: html
        self.term = term  # String: F or S
        self.program = program  # String: e.g. CSC
        self.year = str(year)
        # 100/200/300/400, 0 for all levels of courses by default
        self.level = level  # Int: e.g. 108
        self.credit = credit  # H or Y
        self.campus = "1"  # only for St.george at the moment

    def set_term(self, term):
        self.term = term

    def set_program(self, program):
        self.program = program

    def set_year(self, year):
        self.year = year

    def set_level(self, level):
        self.level = level

    def get_cache(self):
        return self.page_cache

    def get_addresses(self):
        return self.address_book

    def address_construct(self):

        if self.term == "F":
            season = 9
        elif self.term == "S":
            season = 1
        else:
            season = 9

        # finding all possible course code for this level, there will be lots of "unreal" course
        if self.level == 0:
            self.set_level(100)
            gap = 300
        else:
            gap = 100
        # for code in range(self.level, self.level + gap):
        course_list = [104, 108, 148, 165] # for testing purpose
        for course in course_list:
            course_code = self.program + str(course)
            self.address_book[course_code] = \
                self.domain + course_code + self.credit + self.campus + self.term + self.year + str(season)

    def request_url(self):
        header = {'User Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
        for course in self.address_book:
            request = urllib2.Request(self.address_book[course], None, header)
            response = urllib2.urlopen(request)
            html = response.read()
            self.page_cache[course] = html

    def _request_urls(self, dic):
        header = {'User Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.3valu6'}
        for course in dic:
            request = urllib2.Request(dic[course], None, header)
            response = urllib2.urlopen(request)
            html = response.read()
            self.page_cache[course] = html




