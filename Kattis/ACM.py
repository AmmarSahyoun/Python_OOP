

solved = []
total = []
failed = []

while True:
    line = input().split()
    if line[0] == '-1':
        break
    if line[2] == 'right' :
        solved.append(line[1])
        total.append(int(line[0]))
    if line[2] == 'wrong' :
        failed.append(line[1])
for i in failed:
    if i in solved :
        total.append(20)
print(len(solved), sum(total))
