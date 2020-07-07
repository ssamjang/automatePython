#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points
# to the start of each line of text on clipboard

import pyperclip
text = pyperclip.paste()

# TODO: Separate lines and add stars

pyperclip.copy(text)