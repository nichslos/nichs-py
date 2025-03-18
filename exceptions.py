#Exception Exercise 1
try:
    x = int(input("What's x? "))
except ValueError:
     print("x is not a integer")
else:
    print(f"x is {x}")

#Exception Exercise 2

while True:
    try:
        y = int(input("What's y? "))
    except ValueError:
        print("y is not an integer")
    else:
        break
print(f"y is {y}")

#Exception Exercise 3
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not a integer")
        else:
            return x

main()

#Exception Exercise 3
def main1():
    x = get_int1()
    print(f"x is {x}")

def get_int1():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass

main1()

#Exception Exercise 4
def main2():
    x = get_int1("What's x? ")
    print(f"x is {x}")

def get_int2(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main2()