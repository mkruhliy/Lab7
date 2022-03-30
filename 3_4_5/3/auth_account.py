"""Registration and Authorisation"""

import sys

class InvalidNumber(Exception):
    pass

class Banned(Exception):
    pass

class NotBanned(Exception):
    pass

class NoUsername(Exception):
    pass

class NoPassword(Exception):
    pass

class InvalidName(Exception):
    pass

class InvalidPassword(Exception):
    pass

class UserNameAlreadyExists(Exception):
    pass

class PasswordTooShort(Exception):
    pass

class AccountManager:
    """Main features"""

    def __init__(self, file=''):
        self.file = file
        self.choices = {'1': self.register, '2':self.auth, '3':self.quit}

    def display_auth(self):
        """To show options"""
        print("""1) register\n2) authorisation\n3) <<quit>>""")

    def quit(self):
        """Interrupting programme"""
        print("Thank you for using your notebook today.")
        sys.exit(0)

    def write(self, username, password):
        """New users adding"""
        try:
            with open(self.file, 'a') as file:
                file.write('\n{}:{}'.format(username, password))
        except FileNotFoundError:
            print("Can't open file - check if 'accounts.py' is in your current working directory")
            sys.exit(0)

    def data(self):
        """Reading file into dictionary"""
        data = {}
        try:
            with open(self.file, 'r') as file:
                file.readline()
                for elem in file.readlines():
                    i, j = elem.split(':')
                    data[i] = j.split('\n')[0]
            return data
        except:
            print("Can't open file - check if 'accounts.txt' is in your current working directory")
            sys.exit(0)

    def register(self):
        """Registration algorithm"""
        print("\nRegistration form:")
        username = input("username: ")
        password = input("password: ")
        if not username:
            raise NoUsername("Enter a username")
        if not password:
            raise NoPassword("Enter a password")
        if username in self.data().keys():
            raise UserNameAlreadyExists("'{}' username already exists")
        if len(password) < 8:
            raise PasswordTooShort("Password too short")
        else:
            self.write(username, password)
            print("\nSuccessfully registered\nNow you can log in:\n")
            self.auth()

    def chng_permission(self, usr, permission):
        """Banning/Unbanning"""
        if permission not in ['1', '2', 'ban', 'unban']:
            raise InvalidNumber('Enter correct number')
        if (usr not in self.data().keys()) or ('admin' in usr):
            raise InvalidName('Enter valid name')
        with open(self.file, 'r') as file:
            dt = file.readlines()
        for elem in dt:
            if elem.split(':')[0] == usr:
                dt.remove(elem)
                if dt[-1].endswith('\n'):
                    dt[-1] = dt[-1][:-1]
                if permission in ['1', 'ban']:
                    if '(banned)' in elem:
                        raise Banned('Already banned')
                    if '\n' in elem:
                        dt.append('\n'+elem[:-1]+'(banned)')
                    else:
                        dt.append('\n'+elem+'(banned)')
                    print('Successfully banned')
                elif permission in ['2', 'unban']:
                    if '(banned)' not in elem:
                        raise NotBanned('User is not banned')
                    if '\n' in elem:
                        dt.append('\n'+elem[:-9])
                    else:
                        dt.append('\n'+elem[:-8])
                    print("Successfully unbanned")

        with open(self.file, 'w') as file:
            for elem in dt:
                file.write(elem)

    def auth(self):
        """Authorisation algorith"""
        print("\nAuthentication form:")
        username = input("username: ")
        password = input("password: ")
        if not username:
            raise NoUsername("Enter a username")
        if not password:
            raise NoPassword("Enter a password")
        if username not in self.data().keys():
            raise InvalidName("{} wasn't found")
        if self.data()[username] != password:
            if 'banned' in self.data()[username]:
                raise Banned('You are banned')
            raise InvalidPassword("password not right")
        else:
            if username.startswith('admin'):
                chs = input("\nWould you like to ban/unban somebody? (y/n):")
                if chs == 'y':
                    while True:
                        usr = input('Username: ')
                        prms = input('1) ban\n2) unban\n>>> ')
                        try:
                            self.chng_permission(usr, prms)
                        except InvalidName:
                            print('Enter correct name')
                        except Banned:
                            print('User already is banned')
                        except NotBanned:
                            print('User is not banned')
                        except InvalidNumber:
                            print('Enter valid number')
                        else:
                            break

    def run(self):
        """Managing"""
        while True:
            self.display_auth()
            choice = input("Enter an option number: ")
            action = self.choices.get(choice)
            if action:
                try:
                    action()
                except NoUsername:
                    print("\nEnter a username\n")
                except NoPassword:
                    print("\nEnter a password\n")
                except InvalidName:
                    print("\nUsername wasn't found\n")
                except InvalidPassword:
                    print("\nInvalid password\n")
                except UserNameAlreadyExists:
                    print("\nUsername already exists\n")
                except PasswordTooShort:
                    print("\nPassword's too short\n")
                except Banned:
                    print("\nYou are banned\n")
                else:
                    break
            else:
                print("\n{0} invalid number\n".format(choice))
