x = input("enter your name: ")
y = input("enter your password: ")
z = input("enter your password again: ")

if y == z:
    if len(y) < 8 or len(z)  < 8:
        print("please reenter your password - it has to be at least 8 characters")
    else:
        print("thank u")
else:
    print("passwords do not match")

