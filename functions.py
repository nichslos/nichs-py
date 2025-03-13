def hello(to):
    print(f"Hello, {to}")

name = input("What's your name")
hello(name) 


#Return Function

def calcSquare(x):
    x = int(input("What's x?"))
    print(f"x squared is {square(x)}")

def square(n):
    return pow(n, 2)

calcSquare(12)