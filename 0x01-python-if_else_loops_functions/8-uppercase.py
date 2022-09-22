#!/usr/bin/python3
def to_upper(character):
if ord(character) >= 97 and ord(character) <= 122:
return (ord(character) - 32)
else:
return ord(character)

def uppercase(string):
string_new = ""
for characteer in string:
string_new += "%c" % to_upper(charaacter)
print("{:s}".format(string_new))
