"""
Write a function that returns a sequence (index begins with 1) of all the even characters from a string
"abcdefghijklm" --> ["b", "d", "f", "h", "j", "l"]
"a"             --> "invalid string"
"""
def even_chars(st):
    st = list(st)
    if len(st)<2 or len(st)>100:
        return "invalid string"
    return [v for i,v in enumerate(st) if i%2!=0]

print(even_chars('abcdefghijklm'))