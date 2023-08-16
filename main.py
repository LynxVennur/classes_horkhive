from mananger import*
from dummy_data import insert_dummy_data

insert_dummy_data()

mng = Mananger()

while True:
    if mng.get_state() == 'StartUp':
        for txt in startup_texts:
            print(txt)

        try:
            opt = int(input('chose your option: '))
        except:
            print(' ')
            print('  ONLY NUMBERS !!!  ')
            print(' ')
            continue

        if opt == 1:
            mng.set_state('SingIn')
        elif opt == 2:
            mng.set_state('SingUp')
        elif opt == 3:
            mng.set_state('ForgotPass')
        elif opt == 4:
            break
        elif opt == 99:
            mng.set_state('DEBUG')

        else:
            print('invalid input')


    elif mng.get_state() == 'SingIn':
        mng.sing_in()
        state = 'StartUp'

    elif mng.get_state() == 'SingUp':
        mng.new_user()
        state = 'StartUp'

    elif mng.get_state() == 'ForgotPass':
        mng.forgot_password()
        state = 'StartUp'

    elif mng.get_state() == 'Logged':
        main_texts = [
            ''
        ]

    elif mng.get_state() == 'DEBUG':
        for joker in db_users:
            print(joker.name+' '+joker.password+' '+joker.email+' ',joker.cpf)

        print(mng.logged)
        mng.set_state('StartUp')

    print(' ')

