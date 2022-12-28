from mkdocs.plugins import Page

import logging
log = logging.getLogger("mkdocs.plugins." + __name__)


class SectionReader:

    def read_section(self, section, nav_map: dict[str, list[Page]]()):
        """
        Read child sections from a navigation item and populate the nav_map dictionary for use when rendering pages.

        This function expectes that the first child of every section represents the page itself and the subsequent children represent the actual page children.
        The scenario below illustrates what this means:
        Section A - this section
            Page - the page representing Section A
            Page - a child page of Section A
            Section B - a child section of Section A
                Page - the page representing Section B, therefore a child page of Section *A* - aha!, didn't expect that, right?
                Page - a child page of Section B
            Page - another child page of Section A
            etc.
        """
        if type(section.children[0]) is Page:
            parent_page = section.children[0] # first child is a page
            log.debug(f"Parent: {parent_page.title}: {parent_page.file.dest_uri}")
            nav_map[parent_page.file.dest_uri] = list[Page]() # init the child list for this page
            for i in range(1, len(section.children)): # iterate over the subsequent children
                child_candidate = section.children[i] # whe don't know waht this child is
                child_page = None
                if type(child_candidate) is Page: # is it a page? 
                    child_page = child_candidate # the child page is the child itself
                elif type(child_candidate).__name__ == "Section" and child_candidate.children and type(child_candidate.children[0]) is Page: # is the candidate a section? does it have a child and is the child a page?
                    child_page = child_candidate.children[0] # the page is the first child of the section
                log.debug(f"  Child: {child_page.title}: {child_page.file.dest_uri}")
                nav_map[parent_page.file.dest_uri].append(child_page) # insert the child page to the navigation map
