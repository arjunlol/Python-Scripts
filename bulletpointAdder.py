#! python3
# bulletPointAdder.py - Adds wiki bullet points to start
# of each line of text on clipboard

import pyperclip
text = pyperclip.paste()

#sep lines and add stars
lines = text.split('\n')
for i in range(len(lines)):     # loop goes through all indexes in lines list
    lines[i] = '* ' + lines[i]  # add star to each string in lines list    
text = '\n'.join(lines)
pyperclip.copy(text)
