#RegEx Exercise 1 Validation
email = input("What's your email? ").strip()

if "@" in email and "." in email:
    print("valid")
else:
    print("Invalid")

#RegEx Exercise 2 Validation
email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and "." in domain:
    print("valid")
else: 
    print("invalid")

#RegEx Exercise 3 Validation
email = input("What's your email? ").strip()

username, domain = email.split("@")

#Any domains in endswith()
if username and domain.endswith(".edu"):
    print("valid")
else: 
    print("invalid")

#RegEx Exercise 4 Validation
#Import re library
import re

email = input("What's your email? ").strip()

#re.search(pattern, string, flags=0)
#Pattern List
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetitions
# {m} m repetitions
# {m,n} m-n repetitions
if re.search("@", email):
    print("valid")
else:
    print("invalid")

#RegEx Exercise 5 Validation
#Import re library
import re

email = input("What's your email? ").strip()

#re.search(pattern, string, flags=0)
#Pattern List
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetitions
# {m} m repetitions
# {m,n} m-n repetitions

#Pattern Left to Right
if re.search(".*@.*", email):
    print("valid")
else:
    print("invalid")

#RegEx Exercise 6 Validation
#Import re library
import re

email = input("What's your email? ").strip()

#re.search(pattern, string, flags=0)
#Pattern List
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetitions
# {m} m repetitions
# {m,n} m-n repetitions

#Pattern Left to Right
if re.search(".+@.+", email):
    print("valid")
else:
    print("invalid")

#RegEx Exercise 7 Validation
#Import re library
import re

email = input("What's your email? ").strip()

#re.search(pattern, string, flags=0)
#Pattern List
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetitions
# {m} m repetitions
# {m,n} m-n repetitions

#Pattern Left to Right
# (\) Either escapes special characters (permitting you to match characters like '*', '?', and so forth)
#raw string using r
if re.search(r".+@.+\.edu", email):
    print("valid")
else:
    print("invalid")


#RegEx Exercise 8 Validation
#Import re library
import re

email = input("What's your email? ").strip()

#re.search(pattern, string, flags=0)
#Pattern List
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetitions
# {m} m repetitions
# {m,n} m-n repetitions
# ^ matches the start of the string
# $ matches the end ot the string or just before the newline at the end of the string

#Pattern Left to Right
# (\) Either escapes special characters (permitting you to match characters like '*', '?', and so forth)
#raw string using r
if re.search(r"^.+@.+\.edu$", email):
    print("valid")
else:
    print("invalid")


#RegEx Exercise 9 Validation
#Import re library
import re

email = input("What's your email? ").strip()

#re.search(pattern, string, flags=0)
#Pattern List
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetitions
# {m} m repetitions
# {m,n} m-n repetitions
# ^ matches the start of the string
# $ matches the end ot the string or just before the newline at the end of the string
# [] set of characters
# [^] complementing the set

#Pattern Left to Right
# (\) Either escapes special characters (permitting you to match characters like '*', '?', and so forth)
#raw string using r
#prevent from sample@@@sample.edu
if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("valid")
else:
    print("invalid")


#RegEx Exercise 10 Validation
#Import re library
import re

email = input("What's your email? ").strip()

#re.search(pattern, string, flags=0)
#Pattern List
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetitions
# {m} m repetitions
# {m,n} m-n repetitions
# ^ matches the start of the string
# $ matches the end ot the string or just before the newline at the end of the string
# [] set of characters
# [^] complementing the set

#Pattern Left to Right
# (\) Either escapes special characters (permitting you to match characters like '*', '?', and so forth)
#raw string using r
#prevent from sample@@@sample.edu
if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("valid")
else:
    print("invalid")

#RegEx Exercise 11 Validation
#Import re library
import re

email = input("What's your email? ").strip()

#re.search(pattern, string, flags=0)
#Pattern List
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetitions
# {m} m repetitions
# {m,n} m-n repetitions
# ^ matches the start of the string
# $ matches the end ot the string or just before the newline at the end of the string
# [] set of characters
# [^] complementing the set

#Pattern Left to Right
# (\) Either escapes special characters (permitting you to match characters like '*', '?', and so forth)
#raw string using r
#prevent from sample@@@sample.edu
#\w a word character
if re.search(r"^\w+@\w+\.edu$", email):
    print("valid")
else:
    print("invalid")

#RegEx Exercise 12 Validation
#Import re library
import re

email = input("What's your email? ").strip()

#re.search(pattern, string, flags=0)
#Pattern List
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetitions
# {m} m repetitions
# {m,n} m-n repetitions
# ^ matches the start of the string
# $ matches the end ot the string or just before the newline at the end of the string
# [] set of characters
# [^] complementing the set
# \d decimal digit
# \D not a decimal digit
# \s whitespace characters
# \S not a whitespace characters
# \w word character... as well as numbers and the underscore
# \W not a word character
# A|B either A or B
# (...) a group
# (?:...) non-capturing version

#Pattern Left to Right
# (\) Either escapes special characters (permitting you to match characters like '*', '?', and so forth)
#raw string using r
#prevent from sample@@@sample.edu
#\w a word character
#add other domains
if re.search(r"^\w+@\w+\.(com|edu|gov|net|org)$", email):
    print("valid")
else:
    print("invalid")

#RegEx Exercise 13 Validation
#Import re library
import re

email = input("What's your email? ").strip()

#re.search(pattern, string, flags=0)
#Pattern List
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetitions
# {m} m repetitions
# {m,n} m-n repetitions
# ^ matches the start of the string
# $ matches the end ot the string or just before the newline at the end of the string
# [] set of characters
# [^] complementing the set
# \d decimal digit
# \D not a decimal digit
# \s whitespace characters
# \S not a whitespace characters
# \w word character... as well as numbers and the underscore
# \W not a word character
# A|B either A or B
# (...) a group
# (?:...) non-capturing version

#Flags
# re.IGNORECASE
# re.MULTILINE
# re.DOTALL

#Pattern Left to Right
# (\) Either escapes special characters (permitting you to match characters like '*', '?', and so forth)
#raw string using r
#prevent from sample@@@sample.edu
#\w a word character
#lower case
if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("valid")
else:
    print("invalid")

#RegEx Exercise 14 Validation
#Import re library
import re

email = input("What's your email? ").strip()

#re.search(pattern, string, flags=0)
#Pattern List
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetitions
# {m} m repetitions
# {m,n} m-n repetitions
# ^ matches the start of the string
# $ matches the end ot the string or just before the newline at the end of the string
# [] set of characters
# [^] complementing the set
# \d decimal digit
# \D not a decimal digit
# \s whitespace characters
# \S not a whitespace characters
# \w word character... as well as numbers and the underscore
# \W not a word character
# A|B either A or B
# (...) a group
# (?:...) non-capturing version

#Flags
# re.IGNORECASE
# re.MULTILINE
# re.DOTALL

#Pattern Left to Right
# (\) Either escapes special characters (permitting you to match characters like '*', '?', and so forth)
#raw string using r
#prevent from sample@@@sample.edu
#\w a word character
#lower case
#add sub-domain
if re.search(r"^\w+@(\w\.)?\w+\.edu$", email, re.IGNORECASE):
    print("valid")
else:
    print("invalid")

#RegEx Exercise 15 Format User

#Pattern List
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetitions
# {m} m repetitions
# {m,n} m-n repetitions
# ^ matches the start of the string
# $ matches the end ot the string or just before the newline at the end of the string
# [] set of characters
# [^] complementing the set
# \d decimal digit
# \D not a decimal digit
# \s whitespace characters
# \S not a whitespace characters
# \w word character... as well as numbers and the underscore
# \W not a word character
# A|B either A or B
# (...) a group
# (?:...) non-capturing version


#removing , after user input their names

name = input("What's your name? ").strip()
if "," in name:
    last, first = name.split(", ?")
    name = f"{first} {last}"
print(f"Hello {name}")

#RegEx Exercise 16 Format User
#re.search(pattern, string, flags=0)
#Pattern List
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetitions
# {m} m repetitions
# {m,n} m-n repetitions
# ^ matches the start of the string
# $ matches the end ot the string or just before the newline at the end of the string
# [] set of characters
# [^] complementing the set
# \d decimal digit
# \D not a decimal digit
# \s whitespace characters
# \S not a whitespace characters
# \w word character... as well as numbers and the underscore
# \W not a word character
# A|B either A or B
# (...) a group
# (?:...) non-capturing version


#capturing matches
#reformatted when using , (Nico, Abapo)
#raw string using r
import re
name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)+$", name)
if matches:
    last, first = matches.group()
    name = f"{first} {last}"
print(f"hello, {name}")


#RegEx Exercise 17 Format User
#re.search(pattern, string, flags=0)
#Pattern List
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetitions
# {m} m repetitions
# {m,n} m-n repetitions
# ^ matches the start of the string
# $ matches the end ot the string or just before the newline at the end of the string
# [] set of characters
# [^] complementing the set
# \d decimal digit
# \D not a decimal digit
# \s whitespace characters
# \S not a whitespace characters
# \w word character... as well as numbers and the underscore
# \W not a word character
# A|B either A or B
# (...) a group
# (?:...) non-capturing version


#capturing matches
#reformatted when using , (Nico, Abapo)
#raw string using r
#using group()
import re
name = input("What's your name? ").strip()
matches = re.search(r"^(.+), *(.+)+$", name)
if matches:
    name = matches.group(2) + " " + matches.group(1) 
print(f"hello, {name}")


#RegEx Exercise 18 Format User

#Pattern List
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetitions
# {m} m repetitions
# {m,n} m-n repetitions
# ^ matches the start of the string
# $ matches the end ot the string or just before the newline at the end of the string
# [] set of characters
# [^] complementing the set
# \d decimal digit
# \D not a decimal digit
# \s whitespace characters
# \S not a whitespace characters
# \w word character... as well as numbers and the underscore
# \W not a word character
# A|B either A or B
# (...) a group
# (?:...) non-capturing version


#capturing matches
#reformatted when using , (Nico, Abapo)
#raw string using r
#using group()
# := walrus operator
import re
name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)+$", name):
    name = matches.group(2) + " " + matches.group(1) 
print(f"hello, {name}")

#RegEx Exercise 19 Extracting Information

#Pattern List
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetitions
# {m} m repetitions
# {m,n} m-n repetitions
# ^ matches the start of the string
# $ matches the end ot the string or just before the newline at the end of the string
# [] set of characters
# [^] complementing the set
# \d decimal digit
# \D not a decimal digit
# \s whitespace characters
# \S not a whitespace characters
# \w word character... as well as numbers and the underscore
# \W not a word character
# A|B either A or B
# (...) a group
# (?:...) non-capturing version

#Get username name only
#Example https://twitter.com/username
#Using replace()
url = input("URL: ").strip()
username = url.replace("https://twitter.com/", "")
print(f"Username: {username}" )


#RegEx Exercise 20 Extracting Information

#Pattern List
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetitions
# {m} m repetitions
# {m,n} m-n repetitions
# ^ matches the start of the string
# $ matches the end ot the string or just before the newline at the end of the string
# [] set of characters
# [^] complementing the set
# \d decimal digit
# \D not a decimal digit
# \s whitespace characters
# \S not a whitespace characters
# \w word character... as well as numbers and the underscore
# \W not a word character
# A|B either A or B
# (...) a group
# (?:...) non-capturing version

#Get username name only
#Example https://twitter.com/username
#Using removeprefix()
url = input("URL: ").strip()
username = url.removeprefix("https://twitter.com/")
print(f"Username: {username}" )

#RegEx Exercise 21 Extracting Information
#re.sub(pattern, repl, string, count=0, flags=0)
#Pattern List
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetitions
# {m} m repetitions
# {m,n} m-n repetitions
# ^ matches the start of the string
# $ matches the end ot the string or just before the newline at the end of the string
# [] set of characters
# [^] complementing the set
# \d decimal digit
# \D not a decimal digit
# \s whitespace characters
# \S not a whitespace characters
# \w word character... as well as numbers and the underscore
# \W not a word character
# A|B either A or B
# (...) a group
# (?:...) non-capturing version

#Get username name only
#Example https://twitter.com/username
import re
url = input("URL: ").strip()

username = re.sub(r"^(https://)?:/(/www.)?\twitter\.com/", "", url)
print(f"Username: {username}")


#RegEx Exercise 22 Extracting Information

#re.search(pattern, string, flags=0)
#Pattern List
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetitions
# {m} m repetitions
# {m,n} m-n repetitions
# ^ matches the start of the string
# $ matches the end ot the string or just before the newline at the end of the string
# [] set of characters
# [^] complementing the set
# \d decimal digit
# \D not a decimal digit
# \s whitespace characters
# \S not a whitespace characters
# \w word character... as well as numbers and the underscore
# \W not a word character
# A|B either A or B
# (...) a group
# (?:...) non-capturing version

#Get username name only
#removing other domain google.com except twitter.com
#Example https://twitter.com/username
#using group()
# := walrus operator
import re
url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+).+$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))


#RegEx Exercise 23 Extracting Information

#re.search(pattern, string, flags=0)
#Pattern List
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetitions
# {m} m repetitions
# {m,n} m-n repetitions
# ^ matches the start of the string
# $ matches the end ot the string or just before the newline at the end of the string
# [] set of characters
# [^] complementing the set
# \d decimal digit
# \D not a decimal digit
# \s whitespace characters
# \S not a whitespace characters
# \w word character... as well as numbers and the underscore
# \W not a word character
# A|B either A or B
# (...) a group
# (?:...) non-capturing version

#Get username name only
#removing other domain google.com except twitter.com
#Example https://twitter.com/username
#using group()
# := walrus operator
import re
url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))

