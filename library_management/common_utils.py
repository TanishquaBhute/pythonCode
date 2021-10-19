import sys
from logger import debug_print
import library
import login
from constants import BOOK_TYPE_ASSIGNED, BOOK_TYPE_AVAILABLE
from config import user_details
from login import Login


def get_display_options_by_user_role(user_role):
    if user_role == 'student':
        print("1.Issue new book: \n2.Submit book: \n3.Change Password: \n4.Exit:")
    elif user_role == 'admin':
        print("1.Register new user: \n2.List of available books: \n3.List of assigned books: \n4.Change user role:")

    option = int(input("Enter your choice: "))
    debug_print(f"User selected option is: {option}", 'get_option_by_user_role')
    return option


def process_student_option1(user_name, book_name=None):
    if book_name:
        library.assign_book(book_name, user_name)
    else:
        available_books = library.get_books(BOOK_TYPE_AVAILABLE)
        if available_books:
            for book in available_books:
                print(f"{available_books.index(book) + 1} {book[0]} by {book[1]} ")
            book_choice = int(input("Select book: ")) - 1
            book_name = available_books[book_choice][0]
            library.assign_book(book_name, user_name)
        else:
            print("Books are not available")


def process_student_option2(user_name, book_name=None):
    if book_name:
        library.submit_book(book_name, user_name)
    else:
        assigned_books = library.get_assigned_books_by_user_name(user_name)
        for book in assigned_books:
            print(f"{assigned_books.index(book)+1}.{book}")
        option = int(input("Enter your choice:"))
        library.submit_book(assigned_books[option-1], user_name)


def process_student_option3(login_details, new_password=None):
    if new_password:
        login_details.user_details[login_details.user_name]['password'] = new_password
        login_details.update_user_details()
        print("Password changed successfully!")
    else:
        new_password = input("Enter new password:")
        login_details.user_details[login_details.user_name]['password'] = new_password
        login_details.update_user_details()
        print("Password changed successfully!")


def process_admin_option1(login_details, new_user_name=None, new_user_role=None, new_user_password=None):
    if new_user_name in login_details.user_details.keys():
        print("User already exist!")
        sys.exit()
    elif new_user_name and new_user_role and new_user_password:
        login_details.user_details[new_user_name] = {'password': new_user_password, 'user_role': new_user_role}
        login_details.update_user_details()
        print(f"New user registered.\nUser name:{new_user_name}\nPassword:{new_user_password}")
    else:
        new_user_name = input("Enter user name:")
        if new_user_name in login_details.user_details.keys():
            print("User already exist!")
        else:
            user_role = input("Enter user role:")
            password = login.generate_new_user_password()
            login_details.user_details[new_user_name] = {'password': password, 'user_role': user_role}
            login_details.update_user_details()
            print(f"New user registered.\nUser name:{new_user_name}\nPassword:{password}")


def process_admin_option2(user_name):
    available_books = library.get_books(BOOK_TYPE_AVAILABLE)
    print(f"Available books are:{available_books}")


def process_admin_option3(user_name):
    assigned_books = library.get_books(BOOK_TYPE_ASSIGNED)
    print(f"Assigned books are:{assigned_books}")


def process_admin_option4(login_details):
    new_user_name = input("Enter user name:")
    login_details.change_user_role(new_user_name)


