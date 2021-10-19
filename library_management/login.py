import string
import random
import config
import constants
from config import seperator
from logger import debug_print


def generate_new_user_password():
    pseudo_user_password = random.sample(list(string.ascii_uppercase), 3)
    pseudo_user_password.extend(random.sample(list(string.ascii_lowercase), 3))
    pseudo_user_password.extend(random.sample(list(string.digits), 2))
    random.shuffle(pseudo_user_password)
    return ''.join(pseudo_user_password)


class Login:
    def __init__(self, uname, upassword):
        self.user_name = uname
        self.user_password = upassword
        self.user_details = {}
        self.prepare_login()
        self.user_role = self.get_user_role(self.user_name)

    def prepare_login(self):
        """
        read credentials and return user details in dict format
        :return: dict
        """
        try:
            with open(config.CREDENTIALS_FILE, 'r') as f:
                lines = f.readlines()
            debug_print(f"{len(lines)} users found in credentials file.")
            for element in lines:
                split = element.split(seperator)
                self.user_details[split[0]] = {'password': split[1], 'user_role': split[2].replace('\n', '')}
        except Exception as ex:
            print("Something went wrong!.")
            debug_print(ex, "prepare_login")

    def verify_login(self):
        """
        accepts user_name user_password and checks with internal user details
        :param
        :return: bool true/false
        """
        debug_print(f"User name:{self.user_name}", 'verify_login')
        debug_print(f"Password:{self.user_password}", 'verify_login')
        if self.user_name in self.user_details and self.user_details[self.user_name]['password'] == self.user_password:
            debug_print(f"User login is verified, {self.user_name}", "verify_login")
            return True
        else:
            debug_print(f"{self.user_name} is not valid user", "verify_login")
            return False

    def get_user_role(self, user_name):
        """
        accepts self.user_name and returns type of user
        :param
        :return: str student/admin
        """

        debug_print(f"User role is {self.user_details.get(user_name, {}).get('user_role', None)}", "get_user_role")
        return self.user_details.get(user_name, {}).get('user_role', None)

    def update_user_details(self):
        """
        update user details in credential file
        :return:
        """
        users_list = []
        for self.user_name, user_detail in self.user_details.items():
            users_list.append(f"{self.user_name}:{user_detail['password']}:{user_detail['user_role']}\n")
        debug_print(f"Updated users list is: {users_list}", 'update_user_details')
        with open(config.CREDENTIALS_FILE, 'w') as file:
            file.writelines(users_list)

    def change_user_role(self, new_user_name, user_role=None):
        if self.get_user_role(new_user_name) == constants.USER_TYPE_ADMIN:
            warning = input(f"Warning: {new_user_name} is admin. Do you want to continue?(y/n):")
            if warning.lower() == 'y':
                if not user_role:
                    user_role = input("Enter user's new role (admin/student):")
                if user_role in ['admin', 'student']:
                    self.user_details[new_user_name]['user_role'] = user_role
                    self.update_user_details()
                    debug_print(f"User role of {new_user_name} changed: {user_role}")
                else:
                    debug_print(f"Invalid user role:{user_role}", "change_user_role")
            else:
                print("Skipping user role change.")
        else:
            if not user_role:
                user_role = input("Enter user's new role (admin/student):")
            if user_role in ['admin', 'student']:
                self.user_details[new_user_name]['user_role'] = user_role
                self.update_user_details()
                debug_print(f"User role of {new_user_name} changed: {user_role}")
            else:
                debug_print(f"Invalid user role:{user_role}", "change_user_role")


if __name__ == '__main__':
    ob = Login('Mukesh', 'mukesh123')
    debug_print(ob.verify_login(), 'login_main')
    debug_print(ob.get_user_role('Mukesh'), 'login_main')

