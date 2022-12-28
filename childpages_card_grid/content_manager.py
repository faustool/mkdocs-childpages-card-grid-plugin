import os

from mkdocs.plugins import Page

from .page_parser import MainTagLocation

class ContentManager:

    def generate_new_content(self, page: Page, child_list: list[Page]) -> str:
        new_content = "<ul>"
        for child in child_list:
            new_content += f"<li><a href=\"{child.file.url_relative_to(page.file)}\">{child.title}</a></li>"
        return new_content + "</ul>"

    def insert_new_content(self, content: str, new_content: str, main_tag_location: MainTagLocation) -> str:
        content_lines = content.splitlines()

        line_str = content_lines[main_tag_location.line]
        being_str = line_str[:main_tag_location.offset]
        end_str = line_str[main_tag_location.offset + 1:]
        content_lines[main_tag_location.line] = being_str + new_content + end_str

        new_output = os.linesep.join(content_lines)

        return new_output

