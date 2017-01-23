# Created by Jordan Ramos
''''
ATM program that might be seen at any local atm

!1/20/17 - 11:01am

'''

dda_balance = 1423.47
sav_balance = 142234.67
pin_number = 12345

print('Welcome to XYZ Bank!')

cust_pin = int(input('Please enter your pin number\n>> '))

def start_menu():
    print('Welcome to XYZ Bank. Please select from the choices below.\n')
    print('''    [1] Balance Inquiry
    [2] Withdrawal
    [3] Transfer
    [4] Deposit''')
    
    cust_choice = int(input('>>....\n'))
    if cust_choice == 1:
        balance()
    elif cust_choice == 2:
        withdrawal()
    elif cust_choice == 3:
        xfer()
    elif cust_choice == 4:
        deposit()
    else:
        print('Please enter a valid selection')



def verifypin():
    tries = 0
    while tries < 3:
        if cust_pin == 12345:
            start_menu()
        else:
            tries += 1
            print("You've entered an incorrect pin, Please try again.\n")
    print('Sorry, you\'ve entered your pin incorrectly too many times. Goodbye.')

def balance():
    print('Which account would you like to get the balance of: [1]Checking, [2] Savings, [3] Other')
    cust_select = int(input('>> '))
    if cust_select == 1:
        print('Your account balance for this account is: ${:,.2f}'.format(dda_balance))
    elif cust_select == 2:
        print('Your account balance for this account is: ${:,.2f').format(sav_balance)
    elif cust_select == 3:
        print('This account has not been set up yet, returning to main menu, please select again')
    else:
        print('Please make a valid selection, returning to main menu')

def withdrawal():
    global dda_balance
    global sav_balance
    print('Which account would you like to withdraw from: [1]Checking, [2] Savings, [3] Other')
    cust_select = int(input('>> '))
    if cust_select == 1:
        cust_wd_amt = float(input('Please enter the amount you wish to withdraw, in multiples of 20\n>> '))
        if cust_wd_amt % 20 != 0:
            print('please enter a multiple of 20')
        else:
            dda_balance -= cust_wd_amt
            if dda_balance - cust_wd_amt > 0:
               print('You have withdrawn ${:,.2f} from your account. Your remaining balance is: ${:,.2f}\n'.format(cust_wd_amt, dda_balance))
            else:
                print('Insufficient funds for this withdrawal.')
    if cust_select == 2:
        cust_wd_amt = float(input('Please enter the amount you wish to withdraw, in multiples of 20\n>> '))
        if cust_wd_amt % 20 != 0:
            print('please enter a multiple of 20')
        else:
            sav_balance -= cust_wd_amt
            if sav_balance - cust_wd_amt > 0:
                print('You have withdrawn ${:,.2f} from your account. Your remaining balance is: ${:,.2f}\n'.format(cust_wd_amt, sav_balance))
            else:
                print('Insufficient funds for this withdrawal.')
                
def xfer():
    print('Please select which account you want to transfer from: [1] checking, [2] savings, [3] other')
    trans_from = int(input('>> '))
    print ('Please select which account you want to transfer to: [1] checking, [2] savings, [3] other')
    trans_to = int(input('>> '))

def deposit():
    global dda_balance
    global sav_balance
    print('Which account would you like to deposit to: [1]Checking, [2] Savings, [3] Other')
    cust_select = int(input('>> '))
    if cust_select == 1:
        deposit_amt = int(input('How much would you like to deposit into this account?'))
        dda_balance += deposit_amt
        print('You deposited ${:,.2f}. Your new account balance is: ${:,.2f}'.format(deposit_amt, dda_balance))
    elif cust_select == 2:
        deposit_amt = int(input('How much would you like to deposit into this account?'))
        sav_balance += deposit_amt
        print('You deposited ${:,.2f}. Your new account balance is: ${:,.2f}'.format(deposit_amt, sav_balance))
    elif cust_select ==3:
        print('This account is not set up yet')
    else:
        print('Please select a valid account')

def begin_program():
    verifypin()
    
    
begin_program()
    
    
        
        
        
        
            
