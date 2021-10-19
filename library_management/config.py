RUN_MODE = 'debug'
BOOKS_FILE = 'books.txt'
CREDENTIALS_FILE = 'credentials.txt'
user_details = {}
books = {}
student_flags = {'-i': 'common_utils.process_student_option1', '-s': 'common_utils.process_student_option2', '-c': 'common_utils.process_student_option3'}
admin_flags = {'-r': 'common_utils.process_admin_option1', '-av': 'common_utils.process_admin_option2', '-as': 'common_utils.process_admin_option3', '-cr': 'common_utils.process_admin_option1'}
seperator = ':'
