#File I/O Exercise 1
names = []

for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f"Hello, {name}")



#File I/O Exercise 2 Write File
name1 = input("What's your name?")

#Write contents and append
file = open("names.txt", "a")
file.write(name1)
file.close


#File I/O Exercise 3 Write File
name2 = input("What's your name?")

#Write contents and append also new line in .txt file
file = open("name2.txt", "a")
file.write(f"{name2}\n")
file.close


#File I/O Exercise 4 Open File
#Add with
name3 = input("What's your name?")

#Write contents and append
with open("name3.txt", "a") as file:
   file.write(f"{name3}\n")

#File I/O Exercise 5 Reads Existing File
#Read File and remove spaces
with open("names.txt", "r") as file:
   for line in file:
       print("hello,", line.rstrip())

#File I/O Exercise 6 Reads Existing File
#Load Names to memory and remove spaces
name4 = []

with open("names.txt") as file:
   for line in file:
       name4.append(line.rstrip())
#Sorting after the names stored in memory
for name in sorted(name4):
    print(f"Hello, {name}")


#File I/O Exercise 7 Reads Existing File
#Load Names to memory and sort, removing spaces
with open("names.txt") as file:
   for line in sorted(file):
       print("Hello,", line.rstrip())

#File I/O Exercise 8 Reads Existing File
#Load Names to memory and removing spaces
name4 = []

with open("names.txt") as file:
   for line in file:
       name4.append(line.rstrip())
#Sorting after the names stored in memory and reverse it
for name in sorted(name4, reverse=True):
    print(f"Hello, {name}")


#File I/O Exercise 9 Reads Existing File
#Load Names to memory and removing spaces
#CSV File
with open("name.csv") as file:
   for line1 in file:
      #Split, parses, reads and interpret csv file
      row, numbers = line1.rstrip().split(",")
      print(f"{row[0]} is in {numbers[1]}")


#File I/O Exercise 10 Reads Existing File
#Load Names to memory and removing spaces
#CSV File
students = []

with open("students.csv") as file:
   for line1 in file:
      #Split, parses, reads and interpret csv file
      #append and sort dictionary
      student1, student2 = line1.rstrip().split(",")
      student = {"student1": student1, "student2": student2}
      students.append(student)

      #Sorting Dictionary
def get_name(student):
   return student["student1"]

def get_name1(student): 
   return student["student2"]   
 
#Sorted iteration
#key get_name() or get_name1
#or change key=lambda student: student[student1]
#reserve is optional to be add if it is needed to be reversed
for student in sorted(students, key=get_name, reverse=True):
   print(f"{student['student1']} is in {student['student2']}")


#File I/O Exercise 11 Reads Existing File
#Load Names to memory and removing spaces
#CSV File
import csv

students = []
#From the import csv
with open("students.csv") as file:
   reader = csv.reader(file)
   for student1, student2 in reader:
      students.append({"student1": student1, "student2": student2})

#reserve is optional to be add if it is needed to be reversed
for student in sorted(students, key=get_name, reverse=True):
   print(f"{student['student1']} is in {student['student2']}")


#File I/O Exercise 12 Reads Existing File
#Load Names to memory 
#CSV File
import csv

student = []
#From the import csv
with open("students1.csv") as file:
   reader = csv.DictReader(file)
   for row in reader:
       student.append(row)

#reserve is optional to be add if it is needed to be reversed
for student in sorted(student, key=lambda student: student["student1"]):
   print(f"{student['name']} is from {student['home']}")

#File I/O Exercise 13 Reads Existing File
#CSV File, update
import csv

name = input("What's you name? ")
home = input("Where's your home? ")

with open("students1.csv", "a") as file:
   writer = csv.writer(file)
   writer.writerow([name,home])

#File I/O Exercise 14 Reads Existing File
#CSV File, update using DictWriter
import csv

name = input("What's you name? ")
home = input("Where's your home? ")

with open("students1.csv", "a") as file:
   writer = csv.DictWriter(file, fieldnames=["name", "home"])
   writer.writerow({"name": name, "home": home})

#File I/O Exercise 15 Reads Image File
#pip install pillow
import sys

from PIL import Image

images =[]

for arg in sys.argv[1:]:
   image = Image.open(arg)
   images.append(image)

images[0].save(
   "costumes.gif" save_all=True, append_images=[images[1]], duration=200, loop=0]
)
#Add more gif gif below
#py file.py costume1.gif costume2.gif