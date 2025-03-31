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
#methods
#Dunder method
#initialize
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    #Constructor
    student = Student(name, house)
    return student
    
if __name__ == "__main__":
    main()

#Object-Oriented Exercise 10
#methods
#Dunder method
#initialize
class Student:
    def __init__(self, name, house):
        #If there is no name
        if not name:
            #Create Exception using raise
            raise ValueError("Missing")
            #Checks Values
        if house not in ["Values List Here"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    #Constructor
    return Student(name, house)
    
if __name__ == "__main__":
    main()

#Object-Oriented Exercise 11
#methods
#Dunder method
#initialize
class Student:
    def __init__(self, name, house):
        #If there is no name
        if not name:
            #Create Exception using raise
            raise ValueError("Missing")
            #Checks Values
        if house not in ["Values List Here"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    #Constructor
    return Student(name, house)
    
if __name__ == "__main__":
    main()

#Object-Oriented Exercise 12
#methods
#Dunder method
#initialize
class Student:
    def __init__(self, name, house, animal):
        #If there is no name
        if not name:
            #Create Exception using raise
            raise ValueError("Missing")
            #Checks Values
        if house not in ["Values List Here"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.animal = animal
    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    animal = input("Animal: ")
    #Constructor
    return Student(name, house, animal)
    
if __name__ == "__main__":
    main()

#Object-Oriented Exercise 13
#methods
#Dunder method
#initialize
class Student:
    def __init__(self, name, house, animal):
        #If there is no name
        if not name:
            #Create Exception using raise
            raise ValueError("Missing")
            #Checks Values
        if house not in ["Values List Here"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.animal = animal
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.animal:
            case "Sample":
                return "1"
            case "Sample 2":
                return "2"
            case "Sample 3":
                return "3"
            case _:
                return ""

def main():
    student = get_student()
    print("Sample!")
    print(student.charm())

def get_student():
    name = input("Name: ")
    house = input("House: ")
    animal = input("Animal: ")
    #Constructor
    return Student(name, house, animal)
    
if __name__ == "__main__":
    main()

#Object-Oriented Exercise 14
#methods
#Dunder method
#initialize
class Student:
    def __init__(self, name, house):
        #If there is no name
        if not name:
            #Create Exception using raise
            raise ValueError("Missing")
            #Checks Values
        if house not in ["Values List Here"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    animal = input("Animal: ")
    #Constructor
    return Student(name, house, animal)
    
if __name__ == "__main__":
    main()

#Object-Oriented Exercise 15
#methods
#Dunder method
#initialize
#properties
class Student:
    def __init__(self, name, house):
        #If there is no name
        if not name:
            #Create Exception using raise
            raise ValueError("Missing")
            #Checks Values
        if house not in ["Values List Here"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    #Getter
    def house(self):
        return self.house

    #Setter
    def house(self, house):
        if house not in ["Values Here"]:
            raise ValueError("Invalid House")
        self.house = house


def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    animal = input("Animal: ")
    #Constructor
    return Student(name, house, animal)
    
if __name__ == "__main__":
    main()

#Object-Oriented Exercise 16
#methods
#Dunder method
#initialize
#properties
class Student:
    def __init__(self, name, house):
        #If there is no name
        if not name:
            #Create Exception using raise
            raise ValueError("Missing")
        self.name = name
        self.house = house
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    #Getter
    #Using @property
    @property
    def house(self):
        return self._house

    #Setter
    #Using .setter
    @house.setter
    def house(self, house):
        if house not in ["Values Here"]:
            raise ValueError("Invalid House")
        self._house = house


def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    animal = input("Animal: ")
    #Constructor
    return Student(name, house, animal)
    
if __name__ == "__main__":
    main()
