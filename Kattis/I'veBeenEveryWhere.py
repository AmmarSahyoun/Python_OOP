
tests = int(input())

for i in range(tests):
    trips = int(input())
    cities = [input() for x in range(trips)]
    cities = set(cities)
    print(len(cities))