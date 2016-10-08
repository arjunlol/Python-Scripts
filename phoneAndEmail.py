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

#email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                #username
    @                                #@ symbol
    [a-zA-Z0-9.-]+                   #domain name
    (\.[a-zA-Z]{2,4})                #dot-something
    )''',re.VERBOSE)

#TODO: find matches in clipboard text
#TODO: copy results to clipboard
