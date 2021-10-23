from app import books


def print_best_books():
    highest_rated = sorted(books, key=lambda x: x.rating * -1)
    for book in highest_rated:
        if book.rating == 5:
            print(f'{book.book}, ({book.rating} stars)')


def print_cheapest_books():
    lowest_price = sorted(books, key=lambda x: x.price)[:10]
    for book in lowest_price:
        print(f'{book.book}, R{book.price}')


book_generator = (x for x in books)


def next_book():
    print(next(book_generator))
