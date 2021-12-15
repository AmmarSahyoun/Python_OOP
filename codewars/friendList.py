"""  filters a list of strings and returns a list with only your friend which have 4 letters """


def friend(x):
    return list(filter(lambda a: len(a)==4, x))


f= ["Sam", "Kieran", "Mark", "Jane"]
print(friend(f))