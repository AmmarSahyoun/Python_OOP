import sys

inp = sys.stdin.read()
line = inp.split("\n")

Jon = line[0]
doctor = line[1]

[print("no") if doctor.count("a") > Jon.count("a") else print("go")]
