import re
from bs4 import BeautifulSoup

from book_locators.page_locator import BooksPageLocator
from parsers.book_parser import BookParser


class BooksPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(BooksPageLocator.LOCATOR)]

    @property
    def page_count(self):
        content = self.soup.select_one(BooksPageLocator.PAGE_COUNT_LOCATOR).string

        expression = 'Page [0-9]+ of ([0-9]+)'
        matches = re.search(expression, content)
        pages = int(matches.group(1))
        return pages

