#! python3

import re, pyperclip

# TODO: Create a regex for phone numbers
re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-000 ext 12345, ext.12345, x.12345

((\d\d\d)|(\(\d\d\d)))?   #area code (optional)

(\s|-)   # first separator

\d\d\d   # first 3 digits

-    # separator

\d\d\d\d    # last 4 digits

(((ext(\.)?\s|x)      # extension (optional
(\d{2,5})))? # Extension number (optional)

''', re.VERBOSE)

# TODO: Create a regex object for email addresses
emailRegex = re.compile(r'''





''')

# TODO: Get the text off the clipboard

# TODO: Extract the email/phone from this text

# TODO: Copy the extracted email/phone to the clipboard
