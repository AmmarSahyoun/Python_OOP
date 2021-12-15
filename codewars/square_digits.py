""" square every digit of a number and concatenate them."""



def square_digits(num):
    sq = [int(i) * int(i) for i in str(num)]
    return ''.join([str(i) for i in sq ])


a = 9119
print(square_digits(a))