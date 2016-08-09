import re

message1 = 'Call me 415-555-1011 tomorrow'
message2 = 'Call me 555-1011 tomorrow'

phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
matchObject = phoneNumRegex.search(message1)
print(matchObject.group())

matchObject = phoneNumRegex.search(message2)
print(matchObject.group())

batRegex = re.compile(r'Bat(wo)*man')
matchObject = batRegex.search('The adventures of Batman')
print(matchObject.group())
matchObject = batRegex.search('The adventures of Batwoman')
print(matchObject.group())
matchObject = batRegex.search('The adventures of Batwowowowowoman')
print(matchObject.group())


regex = re.compile(r'\+\*\?')
matchObject = regex.search('I learned about +*? regex syntax')
print(matchObject.group())

haRegex = re.compile(r'(Ha){3}')
matchObject = haRegex.search('He said HaHaHa')
print(matchObject.group())                       

digitRegex = re.compile(r'(\d){3,5}?')
matchObject = digitRegex.search('1234567')
print(matchObject.group())
