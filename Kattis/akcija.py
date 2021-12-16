import sys

result = 0
inputs = sorted(sys.stdin.read().split('\n')[1:-1], key=int, reverse=True)
books = ([inputs[i:i + 3] for i in range(0, len(inputs), 3)])

for group in books:
    group = [int(x) for x in group]
    if len(group) == 3:
        result += sum(group[:2])
    else:
        result += sum(group)
print (result)