from lxml import etree


# this class is specifically used for UT's Course Finder, and only
# works for Course Finder's html cache

# 2016/07/11, modified so this class should not be used directly
# from user's interface, only need to be called in Crawler
class UTAnalysis:

    # html element id
    not_found_id = "u23_span"
    prerequisite_id = "u50"
    exclusion_id = "u68"
    br_id = "u122"
    term_id = "u158"
    intro_id = "u32"

    def __init__(self, caches):
        self.caches = caches  # course_code: Course

        # Data Extraction
        self.validate()
        self.update()
    
    def _clean_up(self, s):
        """
        remove all extra newline char
        """
        punctuation = "\n\t\r"""
        result = s.strip(punctuation)
        return result

    def update(self):
        self._extract_prerequisites()
        self._extract_exclusion()
        self._extract_intro()
        self._extract_br()

    def validate(self):
        """validate the course info page, if the course does not exists, mark it as hidden, using u23_span element"""
        for course in self.caches:
            tree = etree.HTML(self.caches[course].get_info_page())
            tag = tree.xpath(u'//span[@id="u23_span"]')
            if len(tag) != 0:
                self.caches[course].set_hidden()
    
    # Core function for html analyzing

    def _extract_prerequisites(self):
        """extracting the prerequisites for all courses, using u50 element"""
        for course in self.caches:
            tree = etree.HTML(self.caches[course].get_info_page())
            tag = tree.xpath(u'//span[@id="u50"]')
            if len(tag) == 0:
                self.caches[course].set_prerequisites("No prerequisites")
            else:
                text = self._clean_up(tag[0].text)
                self.caches[course].set_prerequisites(text)

    def _extract_exclusion(self):
        for course in self.caches:
            tree = etree.HTML(self.caches[course].get_info_page())
            tag = tree.xpath(u'//span[@id="u68"]')
            if len(tag) == 0:
                self.caches[course].set_exclusions("No exclusion")
            else:
                text = self._clean_up(tag[0].text)
                self.caches[course].set_exclusions(text)

    def _extract_br(self):
        for course in self.caches:
            tree = etree.HTML(self.caches[course].get_info_page())
            tag = tree.xpath(u'//span[@id="u122"]')
            if len(tag) == 0:
                self.caches[course].set_br("No br")
            else:
                text = self._clean_up(tag[0].text)
                self.caches[course].set_br(text)

    def _extract_intro(self):
        for course in self.caches:
            tree = etree.HTML(self.caches[course].get_info_page())
            tag = tree.xpath(u'//span[@id="u32"]')
            if len(tag) == 0:
                self.caches[course].set_intro("No Introduction Available")
            else:
                text = self._clean_up(tag[0].text)
                self.caches[course].set_intro(text)




