#! python3
# strongPwCheck.py - checks whether the user password is strong
# at least 8 char and contains a special char

import re, pyperclip

# Compile relevant regex objects
charLowerRegex = re.compile(r'[a-z]')   # Check for lower case
charUpperRegex = re.compile(r'[A-Z]')   # Check for Upper case
numRegex = re.compile(r'\d')            # Check for number
specialRegex = re.compile(r'[\W]')      # Check for special number

pwText = str(pyperclip.paste())         # assigns the text thats on clipboard to pwText

LowerMatch = re.search(charLowerRegex, pwText)  # re.search(pattern, text) returns True or False
UpperMatch = re.search(charUpperRegex, pwText)  # if it encounters ONE instance of the patterns
NumMatch = re.search(numRegex, pwText)
SpecialMatch = re.search(specialRegex, pwText)

if len(pwText) > 7:
    if LowerMatch:
        if UpperMatch:
            if NumMatch:
                if SpecialMatch:
                    print("Password is strong")
                else:
                    print("Password should have at least 1 special character")
            else: 
                print("Password should have at least 1 number")
        else:
            print("Password should have at least 1 Upper case")
    else:
        print("Password should have at least 1 Lower case")
else:
    print("Password should be at least 8 characters long")