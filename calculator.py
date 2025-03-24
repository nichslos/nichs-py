#Unit Test Exercise 1 See calculator1.py
#This is moduile
def main():
    x = int(input("What's x?" ))
    print("x squared is ", square(x))

def square(n):
    return n * n


if __name__ == "__main__":
    main()