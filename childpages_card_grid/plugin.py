"""
Copyright 2023 Jose Fausto Almeida de Oliveira Filho
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

from mkdocs.config import base
from mkdocs.config import config_options as c
from mkdocs.plugins import BasePlugin, Navigation, Page

from .content_manager import ContentManager
from .page_parser import PageParser
from .section_reader import SectionReader

import logging
log = logging.getLogger("mkdocs.plugins." + __name__)


class ChildPagesCardGridPluginConfig(base.Config):
    include_all = c.Type(bool, default=True)

class ChildPagesCardGridPlugin(BasePlugin[ChildPagesCardGridPluginConfig]):

    # prevent reading the navigation map over and over again
    read = False

    # contains a map of child pages
    nav_map = dict[str, list[Page]]()

    # manages the html manipulation
    content_manager = ContentManager()

    # read the navigation map
    section_reader = SectionReader()

    def __init__(self):
        self.enabled = True


    def on_pre_build(self, config) -> None:
        """
        Clean the navigation map to read it again before every build
        """
        self.nav_map.clear()
        self.read = False


    def on_page_context(self, context, page, config, nav: Navigation):
        """
        Populate the navigation map
        """
        if not self.read: 
            for item in nav:
                self.read_item(item)

        self.read = True

        return context


    def read_item(self, item):
        """
        Recursively read items from the navigation object
        """
        if item:
            if type(item).__name__ == "Section":
                self.section_reader.read_section(item, self.nav_map)

            if item.children:
                for child in item.children:
                    self.read_item(child)


    def on_post_page(self, output: str, config, page: Page):
        """
        Insert the children grid card into the page after the main tag
        """
        if 'childpages_card_grid' in page.meta:
            log.info(f"{page.title} has metadata")


        if page.file.dest_uri in self.nav_map:
            child_list = self.nav_map[page.file.dest_uri]
            if len(child_list) > 0:
                # find the main tag in the output html
                page_parser = PageParser()
                page_parser.feed(output)

                if page_parser.article_closing_tag_location:
                    new_content = self.content_manager.generate_new_content(page, child_list)
                    new_output = self.content_manager.insert_new_content(output, new_content, page_parser.article_closing_tag_location)
                    return new_output
                    
        return output

