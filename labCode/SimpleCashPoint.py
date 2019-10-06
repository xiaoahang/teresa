import sys

trials = 1


def cashpoint(truepin, balance):
    # start
    # check pin
    # balance or withdraw
    # or mobile top-up
    # catch pin input
    check_pin_trial = check_pin(truepin, 0)
    if check_pin_trial != True:
        return 'WRONG PIN'
    else:
        choose_transaction_type(balance)


# check pin
def check_pin(truepin, trials):
    if trials >= 3:
        print('Your account is now locked!', file=sys.stderr)
        return False
    else:
        pin = input('Please input your PIN : ')
        if pin == truepin:
            print('PIN is right \n')
            return True
        else:
            trials += 1
            print('%s times trial, PIN is wrong \n' % trials)
            if trials < 3:
                print('If you input wrong BIN in for 3 times, your account will bee locked! \n', file=sys.stderr)
            return check_pin(truepin, trials)


# choose transaction type
def choose_transaction_type(balance):
    trans_type = input('Please choose transaction type: \n'
                       '1. balance ;\n'
                       '2. withdraw request;\n'
                       '3. mobile top-up;\n'
                       '4. log out')
    if trans_type == '1':
        return show_balance(balance)
    elif trans_type == '2':
        return withdraw(balance)
    elif trans_type == '3':
        return mobile_top_up(balance)
    elif trans_type == '4':
        return log_out()
    else:
        print('Please choose right transaction type! \n\n')
        choose_transaction_type(balance)


# withdraw
def withdraw(balance):
    withdraw_amount = input('Please input withdraw amount : ')
    if float(withdraw_amount) > float(balance):
        print('Sorry, Balance not enough.\n\n')
        withdraw(balance)
    else:
        new_balance = float(balance) - float(withdraw_amount)
        print('Withdraw success \nYour current balance is %sGPB \n\n' % new_balance)
        choose_transaction_type(new_balance)


# show balance
def show_balance(balance):
    print('Your balance is %sGPB \n\n' % balance)
    choose_transaction_type(balance)


# mobile top-up
def mobile_top_up(balance):
    print('Sorry, the mobile top-up service is unavailable now !\n\n')
    choose_transaction_type(balance)


# log out
def log_out():
    print('Log out success!')
