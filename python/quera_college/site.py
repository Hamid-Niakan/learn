import re
import hashlib


def hash_string(input_string):
    encoded_string = input_string.encode('utf-8')
    sha256_hash = hashlib.sha256()
    sha256_hash.update(encoded_string)
    hashed_string = sha256_hash.hexdigest()
    return hashed_string


class Site:
    def __init__(self, url_address):
        self.url = url_address
        self.register_users = []
        self.active_users = []

    def show_users(self):
        pass

    def register(self, user):
        found_user = next(
            (registered_user for registered_user in self.register_users if registered_user.user_id == user.user_id), None)
        if found_user:
            raise Exception('user already registered')
        self.register_users.append(user)
        return 'register successful'

    def login(self, **kwargs):
        password = kwargs['password']
        username = kwargs.get('username', None)
        email = kwargs.get('email', None)

        def find_in_list(list, condition):
            return next((x for x in list if condition(x)), None)

        already_logged_in_msg = 'user already logged in'
        successful_login_msg = 'login successful'
        invalid_login_msg = 'invalid login'
        if username and email:
            logged_in_user = find_in_list(
                self.active_users, lambda user: user.username == username and user.email == email and user.password == hash_string(password))
            if logged_in_user:
                return already_logged_in_msg
            user = find_in_list(self.register_users, lambda user: user.username ==
                                username and user.email == email and user.password == hash_string(password))
            if not user:
                return invalid_login_msg
            self.active_users.append(user)
            return successful_login_msg
        if username or email:
            logged_in_user = find_in_list(
                self.active_users, lambda user: user.username == username or user.email == email)
            if logged_in_user:
                return already_logged_in_msg
            user = find_in_list(self.register_users, lambda user: (
                user.username == username or user.email == email) and user.password == hash_string(password))
            if not user:
                return invalid_login_msg
            self.active_users.append(user)
            return successful_login_msg

    def logout(self, user):
        for active_user in self.active_users:
            if active_user.user_id == user.user_id:
                self.active_users.remove(active_user)
                return 'logout successful'
        return 'user is not logged in'

    def __repr__(self):
        return "Site url:%s\nregister_users:%s\nactive_users:%s" % (self.url, self.register_users, self.active_users)

    def __str__(self):
        return self.url


class Account:
    def __init__(self, username, password, user_id, phone, email):
        if self.username_validation(username):
            self.username = username
        else:
            raise Exception('invalid username')
        self.set_new_password(password)
        if self.id_validation(user_id):
            self.user_id = user_id
        else:
            raise Exception('invalid code melli')
        if self.phone_validation(phone):
            if len(phone) == 13:
                phone = '0' + phone[3:]
            self.phone = phone
        else:
            raise Exception('invalid phone number')
        if self.email_validation(email):
            self.email = email
        else:
            raise Exception('invalid email')

    def set_new_password(self, password):
        if self.password_validation(password):
            self.password = hash_string(password)
        else:
            raise Exception('invalid password')

    def username_validation(self, username):
        return re.match(r'^[a-zA-Z]+_[a-zA-Z]+$', username)

    def password_validation(self, password):
        return re.search(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$', password)

    def id_validation(self, id):
        if len(id) == 10:
            control_num = int(id[9])
            digits = id[0:9]
            weighted_sum = 0
            current_position = 10
            for num in digits:
                weighted_sum += (current_position * int(num))
                current_position -= 1
            remainder = weighted_sum % 11
            if (remainder < 2 and remainder == control_num) or (remainder >= 2 and control_num == 11 - remainder):
                return True
            return False
        return False

    def phone_validation(self, phone):
        return re.match(r'^(?:\+989|09)\d{9}$', phone)

    import re

    def email_validation(self, email):
        return re.match(r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+\.[a-zA-Z]{2,5}$', email)

    def __repr__(self):
        return self.username

    def __str__(self):
        return self.username


def show_welcome(fn):
    def wrapper(user):
        username = user.username.replace('_', ' ')
        if len(username) > 15:
            username = username[0:15] + '...'
        return fn(username.title())
    return wrapper


def verify_change_password(fn):
    def wrapper(user, old_pass, new_pass):
        if user.password == hash_string(old_pass):
            user.set_new_password(new_pass)
            return fn(user, old_pass, new_pass)
    return wrapper


@show_welcome
def welcome(user):
    return ("welcome to our site %s" % user)


@verify_change_password
def change_password(user, old_pass, new_pass):
    return ("your password is changed successfully.")


account = Account('ali_babaei', 'Aa123123', '0014723069',
                  '+989195159558', 'hniakan@gmail.com')
print(account.email)
