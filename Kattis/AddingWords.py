
import sys

d = {}
for line in sys.stdin.readlines():
    s = line.split()

    if s[0] == 'def':
        d[s[1]] = int(s[2])

    elif s[0] == 'calc':
        added = s[2::2]
        operands = s[3::2]

        value = True
        total = 0
        if s[1] in d:
            total += d[s[1]]
        else:
            value = False
        for i in range(len(operands)):
            if operands[i] in d:
                if added[i] == '+':
                    total += d[operands[i]]
                elif added[i] == '-':
                    total -= d[operands[i]]
            else:
                value = False
                break
        if value and total in d.values():
            for x in d:
                if total == d[x]:
                    print(' '.join(s[1:]), x)
                    break
        else:
            print(' '.join(s[1:]), 'unknown')

    elif s[0] == 'clear':
        d.clear()