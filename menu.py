import functionality


USER_CHOICE = '''Enter one of the following:

-> 'b' to look at highest rated books
-> 'c' to look at cheapest books
-> 'n' to get next available book on catalogue
-> 'q' to quit

Enter your choice: '''

user_choices = {
    'b': functionality.print_best_books,
    'c': functionality.print_cheapest_books,
    'n': functionality.next_book
}


def user_menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b', 'c', 'n'):
            user_choices[user_input]()
        else:
            print('Please enter valid input')
        user_input = input(USER_CHOICE)


user_menu()
