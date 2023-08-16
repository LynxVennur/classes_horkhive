from classes import*
from database import *

startup_texts = [
        '1 sing in',
        '2 sing up',
        '3 forgot password',
        '4 exit'
    ]
sing_in_texts = [
        'username: ',
        'password: '
    ]
sing_up_texts = [
        'username: ',
        'password: ',
        'e-mail; ',
        'cpf: ',
       're-'
    ]

class Mananger:
    def __init__(self):
        self.logged = False
        self.logged_user = None
        self.state = 'StartUp'

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def new_user(self):
        while True:
            cpf = int(input(sing_up_texts[3]))
            cpf_exists = False

            for joker in db_users:
                if joker.cpf == cpf:
                    cpf_exists = True
                    print(' ')
                    print('cpf already exists')

            if cpf_exists == False:
                break

        name = input(sing_up_texts[0])

        while True:
            password = input(sing_up_texts[1])
            re_password = input(sing_up_texts[4] + sing_up_texts[1])

            if password != re_password:
                print('passwords didnt match')
                print()
            else:
                break

        while True:
            email = input(sing_up_texts[2])
            re_email = input(sing_up_texts[4] + sing_up_texts[2])

            if email != re_email:
                print('e-mails didnt match')
                print()
            else:
                break

        db_users.append(User(name, password, email, cpf, db_users.__len__()+1))

    def sing_in(self):
        while True:
            name = input(sing_in_texts[0])
            password = input(sing_in_texts[1])

            for joker in db_users:
                if joker.name == name:
                    if joker.password == password:
                        self.logged_user = joker
                        self.logged = True
                        print('logged')
                        self.state = 'Logged'
                        return

            print(' ')
            print('maybe name or password are wrong')