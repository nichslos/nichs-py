#RegEx Exercise 1 Validation
email = input("What's your email? ").strip()

if "@" in email and "." in email:
    print("valid")
else:
    print("Invalid")
