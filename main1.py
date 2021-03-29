import re

def check_username(username):
    if len(username) > 3 and len(username) <= 8:
        return True
    elif len(username) <= 3:
        print('The username is too short, please create a new username.')
        return False
    elif len(username) >= 9:
        print('The username is too long, please create a new username.')
        return False

def ask_username():
    while True:
        username = input('Enter a username: ')
        if check_username(username):
            return username 

def check_email(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if re.search(regex, email):
        return True
    else:
        print('Please enter a valid email: ')
        return False

def ask_email():
    while True:
        email = input('Enter an email: ')
        if check_email(email):
            return email

def check_password(password):
    if len(password) < 6:
        print('The password is too short.')
        return False
    upper_case = "[A-Z]"
    if re.search(upper_case, password) is None:
        print('The password does not containt uppercase.')
        return False
    lower_case = "[a-z]"
    if re.search(lower_case, password) is None:
        print('The password does not contain lowercase.')
        return False
    symbols = "[!#$%&'()@*+,-./\^_`{|}~]"
    if re.search(symbols, password) is None:
        print('The password does not containt special symbols.')
        return False
    else:
        return True

def ask_password():
    while True:
        password = input('Create a password: ')
        if check_password(password):
            return password

def check_match(password_confirmation):
    if password == password_confirmation:
        return True
    if password != password_confirmation:
        print('The passwords do not match.')
        return False

def ask_confirmation():
    while True:
        password_confirmation = input('Please enter the password again: ')
        if check_match(password_confirmation):
            return password_confirmation

username = ask_username()
email = ask_email()
password = ask_password()
password_confirmation = ask_confirmation()

list = [username, email, password]
print('List: ' + str(list)) 

#writes the list in a text file 'data"
with open('data.txt', 'w') as f:
    for data in list: 
        f.write('%s\n' % data)

