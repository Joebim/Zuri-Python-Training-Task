class budget:
    


    def __init__(self, category, amount):
        
        self.category = category
        self.amount = amount


    def deposit(self):
        print("Deposit amount")
        print("Welcome! How much do you want to deposit?")
        selectedOption_1 = int(input(" input amount \n"))

        print("where do you want to deposit it")
        selectedOption_2 = input(" 1. food  2.clothing  3.entertainment \n")

        if (selectedOption_2 == 1):
            print("your " + category.category + "budget " + "has been credited with " + selectedOption_1)

        elif (selectedOption_2 == 2):
            print("your " + category_1.category + "budget " + "has been credited with " + selectedOption_1)

        elif (selectedOption_2 == 3):
            print("your " + category_2.category + "budget " + "has been credited with " + selectedOption_1)

        else:
            print("invalid selection")

        
    def check_balance():
        print("Check your balance")

        print("What balance do you want to check")
        selectedOption_2 = input(" 1. food  2.clothing  3.entertainment \n")

        if (selectedOption_2 == 1):
            print("your " + category.category + "balance " + "has been credited with " + category.amount)

        elif (selectedOption_2 == 2):
            print("your " + category_1.category + "balance " + "has been credited with " + category_1.amount)

        elif (selectedOption_2 == 3):
            print("your " + category_2.category + "balance " + "has been credited with " + category_2.amount)

        else:
            print("invalid selection")
        
    def withdrawal(self):
         print("Withdraw amount")
        
    def Transfer(self):
        print("Transfer amount")

        selectedOption =  category_1.category

    

        
category = budget("food", "2000")
category_1 = budget("clothing", "5000")
category_2 = budget("entertainment", "10000")

    
#car_1.name = "mercedes"
#car_2.name = "ford"

#car_1.accel()
#car_2.accel()

#print(car_1.car_name)
#print(car_2.car_name)


#print(help(car))
category.deposit()
