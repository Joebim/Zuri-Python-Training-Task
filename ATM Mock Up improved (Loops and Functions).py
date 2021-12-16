# ATM MOCK UP

# name = input ('what is your username? \n')

# allowedUsers = ["joseph","kay","mike"]
# allowedPassword = ["passwordJoseph","passwordKay","passwordMike"]

# if(name in allowedUsers):
#     password = input ("your password \n")
#     userId = allowedUsers.index(name)

#     if(password == allowedPassword[userId]):
#         print("Welcome %s" % name)
#         print('These are the selected options :')
#         print('1. Withdrawal')
#         print('2. Cash deposit')
#         print('3. Transfer')
#         print('4. Inquiry')
#         print('5. Change pin')

#         selectedOption = int(input('Please select an option \n'))
#         if(selectedOption == 1):
            
#             print('1. Current')
#             print('2. Savings')
#             print('3. Fixed deposit')
            
#             selectedOption = int(input('Please select an Account \n'))
#             if(selectedOption <= 3):
            
#                 print('Select Amount \n')
#                 print('1. 500')
#                 print('2. 1000')
#                 print('3. 2000')
#                 print('4. 3000')
#                 print('5. 5000')
#                 print('6. 10000')
#                 print('7. others')

#             transactionOutput = int(input('Please select an amount \n'))

#             if(transactionOutput <= 6):
#                 print('Transaction processing .....')
                
#             if(transactionOutput == 7):
#                 transactionOutput = (input('Please type in required amount \n'))
#                 print('Transaction processing .....')            
                
            
#         elif(selectedOption == 2):
#             SelectDeposit = int(input('How much would you like to deposit? \n'))
#             print('Transaction processing .....')

#         elif(selectedOption == 3):
#             transferAmount = int(input('How much would you like to transfer? \n'))

#             transferAccount = input('Input Recepient account Number: \n')
            
#             print('Select bank')
#             print('1. UBA')
#             print('2. wema')
#             print('3. FBN')
#             print('4. GT Bank')
#             print('5. Fedelity Bank')
#             print('6. FCMB')
#             print('7. Fedelity Bank')

#             bankSelect  = input('Select a bank \n')

#             if(bankSelect >= 7):
#                 print('Transaction processing .....')
            

#         elif(selectedOption == 4): 
#             print('1. Current')
#             print('2. Savings')
#             print('3. Fixed deposit')

#             fixedAmount = 10000 * selectedOption
#             normalAmount = 10000 * selectedOption + 500

#             AccountSelect = int(input('Please select an Account \n'))
            
#             if(AccountSelect <= 3):
#                 print('Your Fixed Amount is %d' % fixedAmount)
#                 print('Your Account Amount is %d' % normalAmount)

#         elif(selectedOption == 5):
#             password = input ("Input old password \n")
#             if(password == allowedPassword[userId]):
            
#                 newPassword = input ("Input new password \n")
#                 confirmPassword = input ("Confirm new password \n")
#                 if(confirmPassword == newPassword):
#                     print('Password Changed!')
#                 else:
#                     confirmPassword = input ("Password not the same, Confirm new password \n")
#                     if(confirmPassword == newPassword):
#                         print('Password Changed!')
#                     else:
#                         print('Password not the same, please try again later')
                    
#             else:
#                 print('Password incorrect, please try again later')
            

#         else:
#             print('invalid option selected please, please try again')

        
        
#     else:
#         print('Password incorrect, please try again later.')

# else:
#     print('Name not found, please try again later')
    
#     print("Name not found, please try again.")


# ATM MOCK UP IMPROVED

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

    print('1. Current')
    print('2. Savings')
    print('3. Fixed deposit')

    accountSelect()

            
def accountSelect():
    selectedOption = int(input('Please select Account Type \n'))

    for current,savings,fixedDeposit in database.items():

        if(current == selectedOption):
            amountSelect()

            if(savings == selectedOption):
                amountSelect()

                if(fixedDeposit == selectedOption):
                    amountSelect()

                else:
                    print("Invalid option selected")
            else:
                print("Invalid option selected")
        else:
            print("Invalid option selected")

    accountSelect()

def amountSelect():
    selectedOption = int(input('Please select Amount \n'))

    select = {
        1: '500',
        2: '1000',
        3: '2000',
        4: '3000',
        5: '5000',
        6: '10000',
        7: 'others'
    }

    return select.get(selectedOption, default = None)

    print('1. 500')
    print('2. 1000')
    print('3. 2000')
    print('4. 3000')
    print('5. 5000')
    print('6. 10000')
    print('7. others')

    selectedOption = int(input('Please select Amount \n'))

    if(selectedOption == 1):
        argument = 1

    elif(selectedOption == 2):
        argument = 2

    elif(selectedOption == 3):
        argument = 3

    elif(selectedOption == 4):
        argument = 4

    elif(selectedOption == 5):
        argument = 5

    elif(selectedOption == 6):
        argument = 6

    elif(selectedOption == 7):
        transactionOutput = (input('Please type in required amount \n'))
        
        print('Transaction processing .....') 

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

