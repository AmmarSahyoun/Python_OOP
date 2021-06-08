
from random import randint
dice1 = []
dice2 = []

print('   ..::Welcom to The Rolling Dices::..')

def roll():
    num = randint(1,6)
    return num

def duplicates(l1, l2):
    matches= [i for i, j in zip(l1, l2) if i == j]
    return matches
# print result with counters

