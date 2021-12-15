""" square every digit of a number and concatenate them."""



def square_digits(num):
    sq = [str(int(i) * int(i)) for i in str(num)]
    return ''.join(sq)


a = 9119
print(square_digits(a))