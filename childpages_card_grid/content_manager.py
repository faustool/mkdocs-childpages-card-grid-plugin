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

import os
from typing import List
from mkdocs.plugins import Page

from .page_parser import ArticleClosingTagLocation


class ContentManager:
    """
    Manage the HTML contents of the pages that are being modified by this plugin
    """

    def generate_cards_div(self, page: Page, child_list: List[Page]) -> str:
        """
        Generate the div containing all cards
        """
        new_content = '<div class="cards">'
        for child in child_list:
            new_content += f'<a href="{child.file.url_relative_to(page.file)}">'
            new_content += '<div class="card"><div class="card_container">'
            new_content += f'<p>{child.title}</p>'
            new_content += '</div></div></a>'
            new_content += os.linesep
        new_content += '</div>'
        return new_content

    def insert_new_content(self, content: str, new_content: str,
                           article_closing_tag_location: ArticleClosingTagLocation) -> str:
        """
        Takes a content string and adds the new_content to it in the correct position,
        given the article_closing_tag_location
        """
        content_lines = content.splitlines()

        line_str = content_lines[article_closing_tag_location.line - 1]
        being_str = line_str[:article_closing_tag_location.offset - 1]
        end_str = line_str[article_closing_tag_location.offset:]
        content_lines[article_closing_tag_location.line -
                      1] = being_str + new_content + end_str

        new_output = os.linesep.join(content_lines)

        return new_output
