import random
import validation
import database
from getpass import getpass



def init():

    
    print("Welcome to VBank")

    have_account = int(input("Do yo have account with us: 1 (yes) 2 (no) \n"))

    if have_account == 1:
        
        login()
    elif have_account == 2:
        
        register()
    else:
        print("You have selected invalid option")
        init()


def register():
    print("****** Register ******")
    email = input("Enter email address: \n")
    first_name = input("Enter first name: \n")
    last_name = input("Enter last name: \n")
    # password = input("Enter password: \n")
    password = getpass("Enter password: \n")


    # try:
            
    account_number = generate_account_number()

    is_user_created = database.create(account_number, first_name, last_name, email, password)

    # using database module to create new user record

    if is_user_created:

        print("Your account has been created")
        print(" == ==== ====== ===== ===")
        print("Your account number is: %d" % account_number)
        print("Keep your details safe")
        print(" == ==== ====== ===== ===")

        login()

    else:
        print("something went wrong, please try again")

        register()


def login():
    print("********* Login *********")

    account_number_from_user = input("Enter account number: \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        # password = input("Enter password: \n")
        password = getpass("Enter password: \n")

        user = database.authenticated_user(account_number_from_user, password)

        if user:
            bank_operation(user)

        # for account_number, user_details in database.items():
        #     if account_number == int(account_number_from_user):
        #         if user_details[3] == password:
        #             bank_operation(user_details)

        print("Invalid account or password")
        login()
    
    else:
        print("Invalid account number")
        init()


def bank_operation(user):
    print("Welcome %s %s " % ( user[0], user[1] ))
    
    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) logout (4) exit \n"))

    if selected_option == 1:
            
        deposit_operation()
    elif selected_option == 2:
            
        withdrawal_operation()
    elif selected_option == 3:
        
        logout()
    elif selected_option == 4:
            
        exit()
    else:
        
        print("Invalid option selected")
        bank_operation(user)


def withdrawal_operation():
    print("Withdrawal")
    # get current balance
    # get amount to withdraw
    # check if current balance > withdraw amount
    # deduct withdrawn amount from current balance
    # display current balance


def deposit_operation():
    print("Deposit")
    # get current balance
    # get deposit amount
    # add deposited amount to current balance
    # display current balance


def generate_account_number():
    #print("Generating Account Number")
    return random.randrange(1111111111,9999999999)


def get_current_balance(user_details):
    return user_details[4]


def get_current_balance(user_details, balance):
    user_details[4] = balance


def logout():
    login()


init()