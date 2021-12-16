

name = input ('what is your username? \n')

allowedUsers = ["joseph","kay","mike"]
allowedPassword = ["passwordJoseph","passwordKay","passwordMike"]

if(name in allowedUsers):
    password = input ("your password \n")
    userId = allowedUsers.index(name)

    if(password == allowedPassword[userId]):
        print("Welcome %s" % name)
        print('These are the selected options :')
        print('1. Withdrawal')
        print('2. Cash deposit')
        print('3. Transfer')
        print('4. Inquiry')
        print('5. Change pin')

        selectedOption = int(input('Please select an option \n'))
        if(selectedOption == 1):
            
            print('1. Current')
            print('2. Savings')
            print('3. Fixed deposit')
            
            selectedOption = int(input('Please select an Account \n'))
            if(selectedOption <= 3):
            
                print('Select Amount \n')
                print('1. 500')
                print('2. 1000')
                print('3. 2000')
                print('4. 3000')
                print('5. 5000')
                print('6. 10000')
                print('7. others')

            transactionOutput = int(input('Please select an amount \n'))

            if(transactionOutput <= 6):
                print('Transaction processing .....')
                
            if(transactionOutput == 7):
                transactionOutput = (input('Please type in required amount \n'))
                print('Transaction processing .....')            
                
            
        elif(selectedOption == 2):
            SelectDeposit = int(input('How much would you like to deposit? \n'))
            print('Transaction processing .....')

        elif(selectedOption == 3):
            transferAmount = int(input('How much would you like to transfer? \n'))

            transferAccount = input('Input Recepient account Number: \n')
            
            print('Select bank')
            print('1. UBA')
            print('2. wema')
            print('3. FBN')
            print('4. GT Bank')
            print('5. Fedelity Bank')
            print('6. FCMB')
            print('7. Fedelity Bank')

            bankSelect  = input('Select a bank \n')

            if(bankSelect >= 7):
                print('Transaction processing .....')
            

        elif(selectedOption == 4): 
            print('1. Current')
            print('2. Savings')
            print('3. Fixed deposit')

            fixedAmount = 10000 * selectedOption
            normalAmount = 10000 * selectedOption + 500

            AccountSelect = int(input('Please select an Account \n'))
            
            if(AccountSelect <= 3):
                print('Your Fixed Amount is %d' % fixedAmount)
                print('Your Account Amount is %d' % normalAmount)

        elif(selectedOption == 5):
            password = input ("Input old password \n")
            if(password == allowedPassword[userId]):
            
                newPassword = input ("Input new password \n")
                confirmPassword = input ("Confirm new password \n")
                if(confirmPassword == newPassword):
                    print('Password Changed!')
                else:
                    confirmPassword = input ("Password not the same, Confirm new password \n")
                    if(confirmPassword == newPassword):
                        print('Password Changed!')
                    else:
                        print('Password not the same, please try again later')
                    
            else:
                print('Password incorrect, please try again later')
            

        else:
            print('invalid option selected please, please try again')

        
        
    else:
        print('Password incorrect, please try again later.')

else:
    print('Name not found, please try again later')
    
    print("Name not found, please try again.")


