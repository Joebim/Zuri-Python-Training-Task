# Register
# - First name, Last name, Email and password
# - generate user id

# login
# - [username or email] and password

# Bank Operations

# Initializing the System

import random

database = {} #Dictionary

def init():

    print("Welcome to Strad Bank")


    haveAccount = int(input("Do you have an Account with us: 1 (yes) 2 (no) \n"))

    if(haveAccount == 1):
        login()

    elif(haveAccount == 2):
        register()

    else:
        print("You have selected an invalid option")
        init()

def login():

    print("******* Login *******")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password? \n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
            else:
                print('Invalid account password')
        else:
            print('Invalid account number')

    login()


def register():
    print("******* Register *******")
    email = input("What is your email address \n")
    firstName = input("What is your first name \n")
    lastName = input("What is your last name \n")
    password = input("Create a password \n")

    accountNumber = generateAccountNumber()

    database[accountNumber] = [firstName, lastName, email, password]

    print("Your account has been created")
    print(" == ==== ====== ===== === ")
    print("Your account number is %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == === ==== ====== ==== ")

    login()

def bankOperation(user):

    print("Welcome %s %s" % ( user[0], user[1] ) )

    selectedOption = int(input("What would you like to do?  (1) Withdrawal  (2) Cash deposit  (3) Transfer  (4) Inquiry  (5) Change pin (6) Logout  (7)Exit \n"))

    if(selectedOption == 1):
        withdrawalOperation()

    elif(selectedOption == 2):
        deposit()

    elif(selectedOption == 3):
        transfer()

    elif(selectedOption == 4): 
        inquiry()

    elif(selectedOption == 5):
       changePin()

    elif(selectedOption == 6):
       logout()

    elif(selectedOption == 7):
        exit()

    else:
        print("Invalid option selected")
        bankOperation(user)
        

def withdrawalOperation():
    print("Withdrawal")

def deposit():
    print("Deposit Operations")

def transfer():
    print("Transfer")

def inquiry():
    print("Inquiry")

def changePin():
    print("Change Pin")

def exit():
    print("Thank you for banking with us!")

def generateAccountNumber():

    
    return random.randrange(1111111111,9999999999)

def logout():
    login()


##### ACTUAL BANKING SYSTEM ######

init()