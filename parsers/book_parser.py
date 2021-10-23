import re

from book_locators.book_locators import Locators


class BookParser:
    RATING = {
        'One': 1,
        'Two': 2,
        'Three':3,
        'Four':4,
        'Five':5
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"<Book '{self.book}' costs {self.price}, {self.rating} star(s)"

    @property
    def book(self):
        locator = Locators.TITLE
        title_get = self.parent.select_one(locator)
        title = title_get.attrs['title']
        return title

    @property
    def price(self):
        locator = Locators.PRICE
        price_string = self.parent.select_one(locator).string

        expression = '£([0-9]+\.[0-9]+)'
        matches = re.search(expression, price_string)
        return float(matches.group(1))

    @property
    def rating(self):
        locator = Locators.RATING
        beta_rating = self.parent.select_one(locator)
        classes = beta_rating.attrs['class']
        star_rating = [e for e in classes if e != 'star-rating']
        rating_number = BookParser.RATING.get(star_rating[0])
        return rating_number

    @property
    def link(self):
        locator = Locators.LINK
        link_get = self.parent.select_one(locator).attrs['href']
        return link_get
