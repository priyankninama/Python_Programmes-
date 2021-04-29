import re

NAME = re.compile(r"[a-zA-Z]+")
EMAIL = re.compile(r"[^@]+@[^@]+\.[^@]+")
PHONE = re.compile(r"[6-9]{1}[0-9]{9}")
while True:
    name = input('Enter Name: ')
    if not NAME.match(name):
        print("Please Enter Valid Name")
    else:
        break
while True:
    email = input('Enter Email: ')
    if not EMAIL.match(email):
        print("Please enter Valid Email address %s" % (name))
    else:
        break
while True:
    phone = input("Enter Mobile Number : ")
    if not PHONE.match(phone):
        print("Please Enter valid Phone Number %s" % (name))
    else:
        break
print("\nHere are Your Details you Entered\n")
print("Name : %s\nEmail : %s\nPhone Number : %s" % (name, email, phone))
