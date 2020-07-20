#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses
# on the clipboard

import pyperclip
import re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?          # area code
    #3 digits OR 3 digits within parentheses
    (\s|-|\.)?                  # separator
    #speparator = space (\s) OR dash (-) OR period (.)
    (\d{3})                     # first 3 digits
    (\s|-|\.)                   # separator
    (\d{4})                     # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
    )''', re.VERBOSE)

# email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # username (alphanumeric and ._%+-) + means any of the preceding group
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # domain name
    (\.[a-zA-Z]{2,4})       # dot-something. {2,4} = match at least 2 and at most 4 of something
    )''', re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())
matches = []
for group in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
