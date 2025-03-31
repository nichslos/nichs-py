#Object-Oriented Exercise 1
name = input("Name: ")
house = input("House: ")
print(f"{name} from {house}")

#Object-Oriented Exercise 2
def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")

def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

if __name__ == "__main__":
    main()

#Object-Oriented Exercise 3
def main():
    name, house = get_student()
    print(f"{name} from {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house

if __name__ == "__main__":
    main()

#Object-Oriented Exercise 3
#using tuple
def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house

if __name__ == "__main__":
    main()

#Object-Oriented Exercise 4
#immutable
#tuple

def main():
    student = get_student()
    if student[0] == "False Value":
        student[1] == "True Value"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]
    
if __name__ == "__main__":
    main()

#Object-Oriented Exercise 5
#using dictionary
#Accesing Keys
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student
    
if __name__ == "__main__":
    main()

#Object-Oriented Exercise 6
#using dictionary

def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}
    
if __name__ == "__main__":
    main()

#Object-Oriented Exercise 7
#using dictionary

def main():
    student = get_student()
    if student["name"] == "False Value":
        student["house"] == "True Value"
    print(f"{student['name']} from {student['house']}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}
    
if __name__ == "__main__":
    main()

#Object-Oriented Exercise 8
#Classes
class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student
    
if __name__ == "__main__":
    main()

#Object-Oriented Exercise 9