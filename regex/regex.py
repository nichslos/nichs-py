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
#lower case
if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("valid")
else:
    print("invalid")