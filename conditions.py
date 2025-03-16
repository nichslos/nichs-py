#cCondition Exercise 1
x = int(input("Input X"))
y = int(input("Input Y"))


if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else :
    print("x is equal to y")

#Condtion Exercise 2
num = int(input("Input num"))
num1 = int(input("Input num"))

if num != num1:
    print("Num is not Equal")
else:
    print("Num is Equal")



#Condition Exercise 3
a = int(input("Input a"))
b = int(input("Input b"))

if a < b or a > b:
    print("a is not equal to b")
else:
    print("x is equal to y")

#Condtion Exercise 4
score = int(input("Score: "))
if score >= 90 and score < 90:
    print("Grade A")
elif score >= 80 and score < 90:
    print("Grade B")

#Condtion Exercise 5 PARITY
x = int(input("What's x "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

#Condition Exercise 6 
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n % 2 == 0 else False
     
main()

#Condition Exercise 7
name = input("Whats you name? ")
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who")
