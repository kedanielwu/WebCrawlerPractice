class Program:

    def __init__(self, name, url, visible=True):
        self.name = name
        self.url = url
        self.visible = visible

    def __repr__(self):
        return "Program Name: {}\n---\nURL: {}\n---\n\n\n".format(self.name, self.url)

    def is_visible(self):
        return self.visible

    def set_hidden(self):
        self.visible = False

    def get_url(self):
        return self.url

    def get_name(self):
        return self.name
