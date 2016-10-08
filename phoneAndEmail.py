#! python3
# phoneAndEmail.py - Find all phone numbers and email address on clipboard

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?               #area code
    (\s|-|\.)?                       #seperator
    (\d{3})                          #first 3 digits
    (\s|-|\.)                        #seperator
    (\d{4})                          #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?   #extension
    )''', re.VERBOSE)

#TODO: create email regex
#TODO: find matches in clipboard text
#TODO: copy results to clipboard
