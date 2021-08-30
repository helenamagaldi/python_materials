print("welcome to the iron bank of Bravoos ATM")

restart = "Y"
chances = 3
balance = 67.14

while chances >= 0:
    pin = int(input("Please enter your 4 Digit Pin"))
    if pin == 1234:
        print("You entered your pin correctly\n")
        while restart not in ("n", "NO", "no", "N"):
            print("Please Press 1 for you balance\n")
            print("Please Press 2 to make a withdrawl\n")
            print("Please Press 3 to pay in\n")
            print("Please Press 4 to return your card\n")
            option = int(input("What would you like to choose?"))
            if option == 1:
                print("Your balance is: ", balance, "\n")
                restart = input("Would you like to go back?")
                if restart in ("n", 'n', "NO", "no"):
                    print("Thank you")
                    break
            elif option == 2:
                print(input("How much would you like to take home today? \n"))
                restart = input("Would you like to go back?")
                if restart in ("n", 'n', "NO", "no"):