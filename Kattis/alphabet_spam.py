import sys

inputs = sys.read().strip("\n")

lows=ups=whites=symbols= 0


for l in  inputs:
    if l.isalpha()==True and l.isupper()==True:
        ups += 1
    elif l.isalpha()==True:
        lows +=1
    elif l == '_':
        whites +=1
    else:
        symbols +=1

print("%0.16f" %(whites/len(inputs)))
print("%0.16f" %(lows/len(inputs)))
print("%0.16f" %(ups/len(inputs)))
print("%0.16f" %(symbols/len(inputs)))



