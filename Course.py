class Course:
    def __init__(self, course_code, term, year, visible=True):
        self.visible = visible
        self.course_code = course_code
        self.info_page = ""  # html file of course
        self.term = term
        self.year = year
        self.intro = ""
        self.br = ""
        self.prerequisites = ""  # list of Course
        self.exclusions = ""  # list of Course

    def __repr__(self):
        return "Course Code: {}\n---\n{}\n---\nPrerequisites: {}\n---\nBR: {}\n---\nExclusion: {}\n\n\n".format(
            self.get_course_code(),
            self.get_intro(), self.get_prerequisites(), self.get_br(), self.get_exclusions())

    # Getters
    def is_visible(self):
        return self.visible

    def get_course_code(self):
        return self.course_code

    def get_term(self):
        return self.term

    def get_year(self):
        return self.year

    def get_intro(self):
        return self.intro

    def get_br(self):
        return self.br

    def get_prerequisites(self):
        return self.prerequisites

    def get_exclusions(self):
        return self.exclusions

    def get_info_page(self):
        return self.info_page

    # Setters
    def set_hidden(self):
        self.visible = False

    def set_info_page(self, html):
        self.info_page = html

    def set_intro(self, intro):
        self.intro = intro

    def set_br(self, br):
        self.br = br

    def set_prerequisites(self, course):
        self.prerequisites = course

    def set_exclusions(self, course):
        self.exclusions = course
