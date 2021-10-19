import config
from logger import debug_print
from config import books
from constants import BOOK_TYPE_AVAILABLE
from constants import BOOK_TYPE_ASSIGNED


def prepare_library():
    """
    read books and return books details in dict format
    :return: dict
    """
    with open(config.BOOKS_FILE, 'r') as file:
        for book_details in file.readlines():
            split = book_details.split(':')
            books[split[0]] = {'author': split[1].replace('\n', ''), 'assigned_to': ''if len(split) == 2 else split[2].replace('\n', '')}

    return books


def get_available_books():
    """
    read books and return available books details
    :return: list of tuple
    """
    available_books = []
    for key, value in books.items():
        if not value['assigned_to']:
            available_books.append((key, value['author']))
    debug_print(f"Total {len(available_books)} available books found", 'get_available_books')
    return available_books


def get_books(book_type='assigned'):
    """
    read books and return available or assigned books details
    :return: list of tuple
    """
    available_books = []
    assigned_books = []
    for key, value in books.items():
        if not value['assigned_to'] and book_type == BOOK_TYPE_AVAILABLE:
            available_books.append((key, value['author']))
        elif value['assigned_to'] and book_type == BOOK_TYPE_ASSIGNED:
            assigned_books.append((key, value['author']))
    debug_print(f"Total {len(available_books)} available books found", f'get_books:{book_type}')
    debug_print(f"Total {len(assigned_books)} assigned books found", f'get_books:{book_type}')
    return available_books if book_type == BOOK_TYPE_AVAILABLE else assigned_books


def assign_book(book_name, user_name):
    """
    assign book to user and update book details
    :param book_name: book name
    :param user_name: user name
    :return:
    """
    try:

        if user_name and not books[book_name]['assigned_to']:
            books[book_name]['assigned_to'] = user_name
            update_books_details()
            print(f"{book_name} is assigned to {user_name}")
            return True
        else:
            return False
    except:
        return False


def update_books_details():
    """
    update books details and update books file
    :return:
    """
    books_list = []
    for book_name, book_details in books.items():
        books_list.append(f"{book_name}:{book_details['author']}:{book_details['assigned_to']}\n")
    with open(config.BOOKS_FILE, 'w') as file:
        file.writelines(books_list)
    debug_print("Book details updated", "update_books_details")


def check_if_assigned(book_name, user_name):
    """
    checks book is assigned to user
    :param book_name:
    :param user_name:
    :return: boolean True/False
    """
    if books[book_name]['assigned_to'] == user_name:
        debug_print(f"{book_name} is assigned to {user_name}", 'check_if_assigned')
        return True
    else:
        debug_print(f"{book_name} is not assigned to {user_name}", 'check_if_assigned')
        return False


def get_assigned_books_by_user_name(user_name):
    """
    get user assigned book list
    :param user_name:
    :return: list
    """
    assigned_books = []
    for book_name, book_details in books.items():
        if book_details['assigned_to'] == user_name:
            assigned_books.append(book_name)
    return assigned_books


def submit_book(book_name, user_name):
    """
    submit book
    :param book_name:
    :param user_name:
    :return:
    """
    try:
        if books[book_name]['assigned_to']== user_name:
            books[book_name]['assigned_to'] = ''
            update_books_details()
            print(f"{book_name} is submitted.")
            return True
        else:
            return False
    except:
        return False

prepare_library()
