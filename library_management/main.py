from login import Login
import library
import stdiomask
import sys
from logger import debug_print
import common_utils
from config import student_flags, admin_flags
from constants import USER_TYPE_STUDENT, USER_TYPE_ADMIN, BOOK_TYPE_AVAILABLE, BOOK_TYPE_ASSIGNED


def process_student(login_details):
    option = common_utils.get_display_options_by_user_role('student')
    if option == 1:
        common_utils.process_student_option1(login_details.user_name)
    elif option == 2:
        common_utils.process_student_option2(login_details.user_name)
    elif option == 3:
        common_utils.process_student_option3(login_details)


def process_admin(login_details):
    option = common_utils.get_display_options_by_user_role('admin')
    if option == 1:
        common_utils.process_admin_option1(login_details)
    elif option == 2:
        common_utils.process_admin_option2(login_details.user_name)
    elif option == 3:
        common_utils.process_admin_option3(login_details.user_name)
    elif option == 4:
        common_utils.process_admin_option4(login_details)


def process(login_details):
    if login_details.user_role == 'admin':
        process_admin(login_details)
    elif login_details.user_role == 'student':
        process_student(login_details)


def raise_error():
    debug_print("Invalid User ", 'raise_error')


if __name__ == '__main__':
    try:
        arguments = sys.argv
        debug_print(f"Arguments:{arguments}", '__main__')
        if len(arguments) == 1:
            uname = input("Enter username: ")
            upassword = stdiomask.getpass(prompt="Enter password: ", mask='*')
            login_details = Login(uname, upassword)
            login_details.verify_login()
            process(login_details)
        elif '-u' in arguments and '-p' in arguments:
            uname = arguments[arguments.index('-u')+1]
            upassword = arguments[arguments.index('-p')+1]
            login_details = Login(uname, upassword)
            login_details.verify_login()
            if login_details.get_user_role(uname) == USER_TYPE_STUDENT:
                for flag, operation in student_flags.items():
                    if flag in arguments:
                        if flag == '-c':
                            eval(f"{operation}(login_details,'{arguments[arguments.index(flag)+1]}')")
                        else:
                            eval(f"{operation}('{uname}','{arguments[arguments.index(flag)+1]}')")
                        debug_print(f'''eval(f"{operation}('{uname}')")''', "___main___")

            elif login_details.get_user_role(uname) == USER_TYPE_ADMIN:
                for flag, operation in admin_flags.items():
                    if flag in arguments:
                        if flag == '-av':
                            available_books = library.get_books(BOOK_TYPE_AVAILABLE)
                            for book in available_books:
                                print(f"{available_books.index(book)+1}. {book}")
                        elif flag == '-as':
                            assigned_books = library.get_books(BOOK_TYPE_ASSIGNED)
                            for book in assigned_books:
                                print(f"{assigned_books.index(book) + 1}. {book}")
                        elif flag == '-cr':
                            login_details.change_user_role(arguments[arguments.index(flag)+1], arguments[arguments.index(flag)+2])
                            print("User role successfully changed!")
                        else:
                            eval(f"{operation}(login_details,'{arguments[arguments.index(flag)+1]}','{arguments[arguments.index(flag)+2]}','{arguments[arguments.index(flag)+3]}')")
                            debug_print(f'''eval(f"{operation}('{arguments[arguments.index(flag)+1]}','{arguments[arguments.index(flag)+2]}','{arguments[arguments.index(flag)+3]}')")''', "___main___")

        else:
            print("You need to provide -u and -p for login ")
    except Exception as ex:
        print("Something went wrong.")
        debug_print(ex)
