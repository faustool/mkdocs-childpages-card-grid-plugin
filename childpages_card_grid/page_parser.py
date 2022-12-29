from html.parser import HTMLParser

class ArticleClosingTagLocation:
    """
    Represents the location of the closing </article> tag in an HTML document.
    """

    line: -1
    offset: -1

    def __init__(self, line: int, offset: int):
        self.line = line
        self.offset = offset

class PageParser(HTMLParser):
    """
    HTML Parser to read an HTML document and locate the closing </article> tag.
    """

    article_closing_tag_location: ArticleClosingTagLocation

    def handle_endtag(self, tag):
        if tag == "article":
            line, offset = self.getpos()
            self.article_closing_tag_location = ArticleClosingTagLocation(line, offset)
