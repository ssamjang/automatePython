#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses
# on the clipboard

import pyperclip, re

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

# TODO: Create email regex

# TODO: Copy results to the clipboard
