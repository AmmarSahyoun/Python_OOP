# Anagram Detection, codewar
def is_anagram(test, original):
    test = sorted(list(test.lower()))
    original = sorted(list(original.lower()))

    if test == original:
        return True
    else:
        return False

#-------------------------

# def is_anagram(test, original):
#     return sorted(original.lower()) == sorted(test.lower())