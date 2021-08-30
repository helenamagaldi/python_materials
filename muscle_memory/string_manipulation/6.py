z = ["apple", "bear", "sea"]

try:
    y = z.index("bears")
except ValueError:
    print("There is an error")
