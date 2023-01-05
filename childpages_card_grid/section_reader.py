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

import logging

from typing import Dict, List
from mkdocs.plugins import Page

LOG = logging.getLogger("mkdocs.plugins." + __name__)


class SectionReader:
    """
    Read child sections from a navigation item and populate the nav_map dictionary for use
    when rendering pages.
    This function expectes that the first child of every section represents the page itself and
    the subsequent children represent the actual page children.
    The scenario below illustrates what this means:
    Section A - this section
        Page - the page representing Section A
        Page - a child page of Section A
        Section B - a child section of Section A
            Page - the page representing Section B, therefore a child page of Section *A*
            Page - a child page of Section B
        Page - another child page of Section A
        etc.
    """

    def read_section(self, section, nav_map: Dict[str, List[Page]]):
        """
        Read the section
        """
        if isinstance(section.children[0], Page):
            parent_page: Page = section.children[0]  # first child is a page
            LOG.debug("Parent: %s: %s", parent_page.title,
                      parent_page.file.dest_uri)
            # init the child list for this page
            nav_map[parent_page.file.dest_uri] = []
            # iterate over the subsequent children
            for i in range(1, len(section.children)):
                # whe don't know waht this child is
                child_candidate = section.children[i]
                child_page = None
                if isinstance(child_candidate, Page):  # is it a page?
                    child_page = child_candidate  # the child page is the child itself
                # is the candidate a section? does it have a child and is the child a page?
                elif type(child_candidate).__name__ == "Section" \
                        and child_candidate.children \
                        and isinstance(child_candidate.children[0], Page):
                    # the page is the first child of the section
                    child_page = child_candidate.children[0]
                LOG.debug("  Child: %s: %s", child_page.title,
                          child_page.file.dest_uri)
                # insert the child page to the navigation map
                nav_map[parent_page.file.dest_uri].append(child_page)
