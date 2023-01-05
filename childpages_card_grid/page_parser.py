"""
Copyright 2023 Fausto Oliveira
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from html.parser import HTMLParser
import logging
import dataclasses

LOG = logging.getLogger("mkdocs.plugins." + __name__)


@dataclasses.dataclass
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
            self.article_closing_tag_location = ArticleClosingTagLocation(
                line, offset)

    def error(self, message: str):
        return LOG.error(message)
