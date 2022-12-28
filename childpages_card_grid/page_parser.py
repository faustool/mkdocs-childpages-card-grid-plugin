from html.parser import HTMLParser

class MainTagLocation:
    """
    Represents the location of the <main> tag in an HTML document.
    """

    line: -1
    offset: -1

    def __init__(self, line: int, offset: int):
        self.line = line
        self.offset = offset

class PageParser(HTMLParser):
    """
    HTML Parser to read an HTML document and locate the <main> tag.
    """

    main_tag_location: MainTagLocation

    def handle_endtag(self, tag):
        if tag == "main":
            line, offset = self.getpos()
            self.main_tag_location = MainTagLocation(line, offset)
