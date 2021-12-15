""" You're given a substring s of some cyclic string. What's the length
of the smallest possible string that can be concatenated to itself many times to obtain this cyclic string?"""


def cyclic_string(s):
    for i in range(1, len(s)):
        if s in s[:i] * len(s):
            return i
    return len(s)

s = "cabca"

print(cyclic_string(s))


# def cyclic_string(s):
#     return next((i for i, _ in enumerate(s[1:], 1) if s.startswith(s[i:])), len(s))