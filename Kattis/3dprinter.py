from math import log, ceil
import sys


num = sys.stdin.read()
num = float(num.strip('\n'))

result = ceil(log(num, 2)+1)
print(result)


# for i in range(1, 20):
#     print(i , '...' , log(i, 2))