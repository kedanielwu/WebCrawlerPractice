import sys
reload(sys)
sys.setdefaultencoding('utf8')


# input content must be a dict, with the format
# key: Object, the object must has attribute visible,
# and method is_visible for deciding the object should be
# included or not
class FileSystem:

    def __init__(self, filename, content):
        self.filename = filename
        self.content = content

    def writing(self):
        file = open(self.filename, 'w')
        for obj in self.content:
            if self.content[obj].is_visible():
                file.write(self.content[obj].__repr__())
        file.close()


