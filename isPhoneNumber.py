#! python3
# Checks if a string matches a specific pattern (phone number format)

#regex
import re 

text = 'My number is 415-555'

def isPhoneNumber(text):
    phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
    mo = phoneNumRegex.search(text)
    if not mo:
        print('No phone numbers found')
    else:
        print('Phone number found: ' + mo.group())

isPhoneNumber(text)