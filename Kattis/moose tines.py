

tines = input().split()

tine1, tine2 = int(tines[0]), int(tines[1])
if tine1==tine2 == 0:
    print('Not a moose')
elif tine1 == tine2:
    print('Even', (tine1+tine2))
else:
    m = max(tine1, tine2)
    print('Odd', int(m) * 2)