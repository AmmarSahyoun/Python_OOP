import re
''' A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern '''

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) # (^start with, $ ends with)
x = re.findall("ai", txt) # find all
x = re.search("\s", txt) # retuns first white space character
#------------Split------------
x = re.split("\s", txt)
x = re.split("\s", txt, 1) # split at the first space
#-----------------sub--------------
x = re.sub("\s", "9", txt) # sub replaces space with 9
x = re.sub("\s", "9", txt, 2) # split just two times
x = re.search(r"\bS\w+", txt)


print(x)