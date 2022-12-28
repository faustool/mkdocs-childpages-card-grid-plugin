import os

from mkdocs.plugins import Page

from .page_parser import ArticleClosingTagLocation

class ContentManager:

    def generate_new_content(self, page: Page, child_list: list[Page]) -> str:
        new_content = '<div class="cards">'
        for child in child_list:
            new_content += f'<a href="{child.file.url_relative_to(page.file)}">'
            new_content += '<div class="card"><div class="card_container">'
            new_content += f'<p>{child.title}</p>'
            new_content += '</div></div></a>'
            new_content += os.linesep
        new_content += '</div>'
        return new_content

    def insert_new_content(self, content: str, new_content: str, article_closing_tag_location: ArticleClosingTagLocation) -> str:
        content_lines = content.splitlines()

        line_str = content_lines[article_closing_tag_location.line - 1]
        being_str = line_str[:article_closing_tag_location.offset -1]
        end_str = line_str[article_closing_tag_location.offset:]
        content_lines[article_closing_tag_location.line - 1] = being_str + new_content + end_str

        new_output = os.linesep.join(content_lines)

        return new_output

