import re

lyrics = ''' 
On the first day of Christmas
my true love sent to me:
12 Drummers Drumming
11 Pipers Piping
10 Lords a Leaping
9 Ladies Dancing
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree'''

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

vowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(vowelRegex.findall(lyrics))

NegativeVowelRegex = re.compile(r'[^aeiouAEIOU]')
print(NegativeVowelRegex.findall(lyrics))

beginsWithHelloRegex = re.compile(r'^Hello')
matchObject = beginsWithHelloRegex.search('Hello There!')
print(matchObject.group())
