""" Gets text from clipboard
    Adds star and space to the beginning of each line
    Pastes new text to clipboard"""

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')

for i in range(len(lines)): # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list

text = '\n'.join(lines)

pyperclip.copy(text)
