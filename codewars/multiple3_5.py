"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. """



def solution(number):
    if number <= 0: return 0
    else:
        r = [i for i in range(1, number) if i%3==0 or i%5==0]
    return sum(r)



a=10
print(solution(a))