# cats = ["mango", "pancakes", "blueberry"]

# for cat in cats:
#     print("meow: ", cat)

# print("Good Bye")

num = int(input("Number: "))
factorial = 1

if num < 0:
    print("must be positive")

elif num == 0:
    print("factorial * i")

else:
    for i in range(1, num + 1):
        factorial = factorial*i

print(factorial)