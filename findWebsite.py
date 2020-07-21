#! python3
# findWebsite.py - Finds websites beginning with https or http

import pyperclip, re

# Find matches that start with http:// or https://
webRegex = re.compile(r'(http(s)?:\/\/\S*)')
# r = raw text
# http(s)? = match http, s is optional
# :\/\/ = match ://
# \S* = match until space/newline
# technically we could've omitted :\/\/ since \S* covers them...

text = str(pyperclip.paste())
matches = []

# Copy results to clipboard
for groups in webRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No websites found.')
