'''A password generator is a tool that creates strong, random passwords to enhance security. Users can
specify criteria such as password length and the inclusion of uppercase letters, lowercase letters,
numbers, and special characters. The generated passwords are typically complex and difficult to guess,
helping to protect user accounts and sensitive information.'''

import random
import string
# Acc to question Users can specify criteria such as password length and the inclusion of uppercase letters, lowercase letters,numbers, and special characters#
length=int(input("Enter password length: "))
include_upper=input("Include UPPERCASE letters? (yes/no):").lower()=='yes'
include_lower=input("Include lowercase letters? (yes/no): ").lower()=='yes'
include_digits=input("Include digits? (yes/no): ").lower()=='yes'
include_special=input("Include special characters (e.g., @#$%)? (yes/no): ").lower()=='yes'
password=""
if include_upper:
   password+=string.ascii_uppercase
if include_lower:
     password+=string.ascii_lowercase
if include_digits:
    password+=string.digits
if include_special:
    password+=string.punctuation

if password=="":
    print("Error:You must have to select at least one character type.")
else:
   for i in range(length):
        password+=random.choice(password)
        print("Generated Password:",password)

   