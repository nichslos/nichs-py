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

#Object-Oriented Exercise 17
#methods
#Dunder method
#initialize
#properties
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    #Getter
    #Using @property
    @property
    def name(self):
        return self._name
    
    #Setter
    #Using .setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

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
    student._house = "Value Here"
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    animal = input("Animal: ")
    #Constructor
    return Student(name, house, animal)
    
if __name__ == "__main__":
    main()

#Object-Oriented Exercise 17
#Showing DATA type
print(type(50))
print(type("Hello, World"))
print(type([]))
print(type(list()))
print(type({}))
print(type(dict()))


#Object-Oriented Exercise 17
#Class Methods
import random

class Hat:
    def __init__(self):
        self.houses = ["Some Value Here"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))

hat = Hat()
hat.sort("Sample")

#Object-Oriented Exercise 18
#Class Methods
import random

class Hat:
    
    houses = ["Some Value Here"]
    #Using @classmethod
    #cls
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Sample")


#Object-Oriented Exercise 19
#Inheritance
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name")
        self.name = name

#Inherit from Wizard
class Student(Wizard):
    def __init__(self, name, house):
       #Refer to parent class or superclass using super()
       super().__init__(name)
       self.house = house

class Professor(Wizard):
    def __init__(self, name, subject):
        #Refer to parent class or superclass using super()
        super().__init__(name)
        self.subject = subject

wizard = Wizard("Sample", "Sample")
student = Student("Sample", "Sample")
professor = Professor("Sample", "Sample")

#Object-Oriented Exercise 20
#Operator Overloading

class Vault:
    def __init__(self, cent=0, peso=0, thousand=0):
        self.cent = cent
        self.peso = peso
        self.thousand = thousand

    def __str__(self):
        return f"{self.cent} Cents, {self.peso}Pes, {self.thousand} Thousand"

coin = Vault(100, 50, 25)
print(coin)


#Object-Oriented Exercise 20
#Operator Overloading

class Vault:
    def __init__(self, cent=0, peso=0, thousand=0):
        self.cent = cent
        self.peso = peso
        self.thousand = thousand

    def __str__(self):
        return f"{self.cent} Cents, {self.peso}Pes, {self.thousand} Thousand"

coin = Vault(100, 50, 25)
print(coin)

coin1 = Vault(100, 50, 25)
print(coin1)

#Add Objects
totalCents = coin.cent + coin1.cent 
totalPeso = coin.peso + coin1.peso 
totalThousands = coin.thousand + coin1.thousand 

total = Vault(totalCents, totalPeso, totalThousands)
print(total)

#Object-Oriented Exercise 21
#Operator Overloading

class Vault:
    def __init__(self, cent=0, peso=0, thousand=0):
        self.cent = cent
        self.peso = peso
        self.thousand = thousand

    def __str__(self):
        return f"{self.cent} Cents, {self.peso}Pes, {self.thousand} Thousand"

    #object._add_(self, other)
    def __add__(self, other):
        cent = self.cent + other.cent
        peso = self.peso + other.peso
        thousand = self.thousand + other.thousand
        return Vault(cent, peso, thousand)

coin = Vault(100, 50, 25)
print(coin)

coin1 = Vault(100, 50, 25)
print(coin1)

#Add Objects


total = coin + coin1
print(total)