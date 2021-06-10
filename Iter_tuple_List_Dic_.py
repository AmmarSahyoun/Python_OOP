###----------------------------------------------###
###         list, tuple, Dict ,iteation          ###
###----------------------------------------------###
# categories = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
# rests = []

# payment = 1000
# bill = 526.38
# change = int(round(1000-bill, 0))
# print(f"the change is: {change} kr.")

# for i in range(len(categories)): # calc the count of exchange
#     count = change // categories[i]
#     rests.append(count)
#     change -= count*categories[i]

# [print(f"{categories[i]}, kr bills: {rests[i]}") for i 
# in range(len(categories))]
# ------------------sum of 5 random------------------
# import random
# numbers=[]

# numbers.append(random.randint(1,100))
# for i in range(5):
#     numbers.append(random.randint(1,100))
# print('the random numbers are:',numbers)
# print('the sum is:', sum(numbers))
#---------------------skatt ----------------------
# tax = 0
# while True:
#     income = float(input('Please Enter monthly income:'))
#     if income <= 0:
#         print(income, 'Enter correct income!')
#         continue
#     else:
#         if income < 38000:
#             tax = income*0.3
#         elif income <50000:
#             income -= 38000
#             tax = 38000*0.3 + income*0.35
#         else:
#             income -= 50000
#             tax = 38000*0.3 + 12000*0.35 + income*0.4
#     print('The corresponding tax is:',tax )
#     break
#-------------------Count digits------------------------
# zeros = 0
# odd =0
# even = 0

# while True:
#     number = int(input('Enter a positive number:'))
#     if number <= 0:
#         print("Wrong! the number should be positive!")
#         continue
#     else:
#         for i in str(number):
#             i = int(i)
#             if i==0: zeros+=1
#             elif i%2 !=0: odd+=1
#             elif i%2 ==0: even+=1
#         print('Zeros:',zeros)
#         print('Odd:',odd)
#         print('Even:',even)
#     break
#---------------------------Guess 10 attempts------------------------
# import random 

# number = random.randint(1,100)
# guesses = 10
# msg = ""

# while guesses > 0:
#     guess = int(input("Guess a number between 1-100: "))
#     if guess > number:
#         print("Clue: go lower")
#         guesses -= 1
#     elif guess < number:
#         print("Clue: go higher")
#         guesses -= 1
#     else:
#         if guesses > 6:
#             msg = "Excellent!"
#         elif guesses > 3:
#             msg = "correct!"
#         else:
#             msg = "correct!"
#         print(f"Correct answer after only {msg} guesses! - {msg}")
#         break

# if guesses == 0:
#     print("Sorry! You lost!")
#-----------------------Pyramid----------------------------------
# number = int(input("Enter a large positive integer: "))
# sum = 1
# total = 0
# if number > 0:
#     while total < number:
#         total += sum
#         sum += 2
#     print(sum-2)
# else:
#     print("The number is not a positive value!")
#---------------------------------------------------
# a = [1,2,3]
# b = a
# del a[0:1]
# print(id(a))
# print(id(b))
#------------------reverse list------------------
# def reverse(list):
#     rev = list[::-1]
#     return rev
# a = reverse([1,2,3])
# print(a)
#--------------------Statistics----------------------
# import random 

# while True:
#     number = int(input("Enter number of integers to be generated: "))
#     if number <=0:
#         print('Wrong!!!')
#         continue
#     else:
#         numbers = [x/x * random.randint(1,100) for x in range(1, number+1)]
#         sum = 0
#         min_num = numbers[0]
#         max_num = numbers[0]

#         print("Generated values: ", end="")
#         for x in numbers:
#             print(int(x), end=" ")
#             sum += x
#             if x > max_num:
#                 max_num = x
#             elif x < min_num:
#                 min_num = x
#         average = sum/number

#         print(f"\nAverage:{average}, min:{int(min_num)}, and max:{int(max_num)}")
#     break
#-----------------------Leap Year--------------------
# def is_year_leap(year):
#     if year%4 == 0:
#         if year %100 == 0:
#             if year %400 == 0:
#                 result = True
#             else:
#                 result = False
#         else:
#             result = True
#     else:
#         result = False
#     return result

# test_data = [1900, 2000, 2016, 1987]     # chck result
# test_results = [False, True, True, False]
# for i in range(len(test_data)):
# 	yr = test_data[i]
# 	print(yr,"->",end="")
# 	result = is_year_leap(yr)
# 	if result == test_results[i]:
# 		print("OK")
# 	else:
# 		print("Failed")
#-------------------------prime number Evaluate Is_True--------------------
# def is_prine(num):
#     for i in range(2, int(1 + num ** 0.5)):
#         if num % i == 0:
#             return False
#     return True
   
# for i in range(1, 20):
# 	if is_prine(i + 1):
# 			print(i +1, end=" ")
# print()
# #--------------------instead of evaluate return result as list-----------------
# def even_num_lst(ran):
#     lst = []
#     for num in range(ran):
#         if num % 2 == 0:
#             lst.append(num)
#     return lst
# print(even_num_lst(11))
#--------------------------------bmi------------------------
# def bmi(weight,  height):
#     return weight/height **2
#------------------Recursion with fibonacci-----------------------
# fibonacci_cache = {}  # memorization; is a way in recursion function not to repeat your work
# def fibonacci(n):
#     if type(n) != int:
#         raise TypeError(' The number should be positive integer')
#     if n <1 :
#         raise ValueError('he number should be positive integer')
#     if n in fibonacci_cache:
#        return fibonacci_cache[n]
#     if n==1: value = 1
#     elif n==2: value = 1
#     elif n > 2:
#         value = fibonacci(n-1)+ fibonacci(n-2)

#     fibonacci_cache[n] = value  # cache the value
#     return value

# for n in range(1,100):
#     print(n, ':', fibonacci(n))
#-------------------Read students'scores and evaluate average scores----------------------------------
# school_class = {}

# while True:
#     name = input("Enter the student's name: /or just press enter to exit!")
#     if name == '':
#         break
#     score = int(input("Enter the student's score (0-10): "))
#     if score not in range(0, 11):
# 	    break
    
#     if name in school_class:
#         school_class[name] += (score,)
#     else:
#         school_class[name] = (score,)
        
# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         counter += 1
#     print("The average of",name, ":", adding / counter)
#-------------------------Tuple count--------------------------------------
# m = []
# d = []
# tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 4
# for i in tup:
#     if i not in d:
#         if tup.count(i) >1:
#             d.append(i)
#         elif i not in m:
#             m.append(i)
# print('one time:', m)
# print('double times:', d)
#----------------------convert tuple to dictionary---------------------------
# colors = (("green", "#008000"), ("blue", "#0000FF"))
# f = dict(colors)
# print(f)
#----------------------------------------------
# my_dictionary = {"A": 1, "B": 2}
# copy_my_dictionary = my_dictionary.copy()
# my_dictionary.clear()
# print(copy_my_dictionary)
#---------------------------------------------------
# colors = {
#     "white": (255, 255, 255),
#     "grey": (128, 128, 128),
#     "red": (255, 0, 0),
#     "green": (0, 128, 0)
#     }
# for col, rgb in colors.items():
#     print(col, ":", rgb)
#-----------------------------Dict manipulate------------------------------
# d = {'one':'two', 'three':'one', 'two':'three'}
# v = d['one']

# for k in range (len(d)):
#     v = d[v]            #trick! nothing todo with loop
   
# print(d[d[v]])
# print(v)
# print(len(d))
#---------------------------slice tuple
# t = (1,2,3,5)
# print(t[1:3])
#--------------------------------
# t = (1,) + (1,)
# t = t + t
# print(len(t))
# print(t)
#-----------------------tic tac toe----------------------------
# from random import randrange

# def display_board(board):
# 	print("+-------" * 3,"+", sep="")
# 	for row in range(3):
# 		print("|       " * 3,"|", sep="")
# 		for col in range(3):
# 			print("|   " + str(board[row][col]) + "   ", end="")
# 		print("|")
# 		print("|       " * 3,"|",sep="")
# 		print("+-------" * 3,"+",sep="")

# def enter_move(board):
# 	ok = False	# fake assumption - we need it to enter the loop
# 	while not ok:
# 		move = input("Enter your move: ") 
# 		ok = len(move) == 1 and move >= '1' and move <= '9' # is user's input valid?
# 		if not ok:
# 			print("Bad move - repeat your input!") # no, it isn't - do the input again
# 			continue
# 		move = int(move) - 1 	# cell's number from 0 to 8
# 		row = move // 3 	# cell's row
# 		col = move % 3		# cell's column
# 		sign = board[row][col]	# check the selected square
# 		ok = sign not in ['O','X'] 
# 		if not ok:	# it's occupied - to the input again
# 			print("Field already occupied - repeat your input!")
# 			continue
# 	board[row][col] = 'O' 	# set '0' at the selected square

# def make_list_of_free_fields(board):
# 	free = []	# the list is empty initially
# 	for row in range(3): # iterate through rows
# 		for col in range(3): # iterate through columns
# 			if board[row][col] not in ['O','X']: # is the cell free?
# 				free.append((row,col)) # yes, it is - append new tuple to the list
# 	return free

# def victory_for(board,sgn):
# 	if sgn == "X":	# are we looking for X?
# 		who = 'me'	# yes - it's computer's side
# 	elif sgn == "O": # ... or for O?
# 		who = 'you'	# yes - it's our side
# 	else:
# 		who = None	# we should not fall here!
# 	cross1 = cross2 = True  # for diagonals
# 	for rc in range(3):
# 		if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:	# check row rc
# 			return who
# 		if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: # check column rc
# 			return who
# 		if board[rc][rc] != sgn: # check 1st diagonal
# 			cross1 = False
# 		if board[2 - rc][2 - rc] != sgn: # check 2nd diagonal
# 			cross2 = False
# 	if cross1 or cross2:
# 		return who
# 	return None

# def draw_move(board):
# 	free = make_list_of_free_fields(board) # make a list of free fields
# 	cnt = len(free)
# 	if cnt > 0:	# if the list is not empty, choose a place for 'X' and set it
# 		this = randrange(cnt)
# 		row, col = free[this]
# 		board[row][col] = 'X'


# board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] # make an empty board
# board[1][1] = 'X' # set first 'X' in the middle
# free = make_list_of_free_fields(board)
# human_turn = True # which turn is it now?
# while len(free):
# 	display_board(board)
# 	if human_turn:
# 		enter_move(board)
# 		victor = victory_for(board,'O')
# 	else:	
# 		draw_move(board)
# 		victor = victory_for(board,'X')
# 	if victor != None:
# 		break
# 	human_turn = not human_turn		
# 	free = make_list_of_free_fields(board)

# display_board(board)
# if victor == 'you':
# 	print("You won!")
# elif victor == 'me':
# 	print("I won")
# else:
# 	print("Tie!")
# ------------------------------------------------------------

d={'one':[1,2,3], 'two':['Jonas', 'Lune', 'Sam']}

# d.update({'one':5})
# d.update({'three':['Ammar']})
# print(d)
#---------------Change key name ------------------------------
# d['g'] = d['one']
# del d['one']
# print(d)
#-----------------------Create dict from list---------------------------
# names = ['Sam', 'Kale', 'Anna', 'Paul']
# series1 = {names.index(x): x for x in (names)}
# print(series1)
#------------------------Create dict and get values as list---------------------------
# f = {x: x*2 for x in range(5)}
# print(f)
# print([f.get(i) for i in f ])  # get values
#--------------------Create Dict from list of names-------------------
# my_dict = {}
# names = ['Jonas', 'Lune', 'Pep']
# for x in range(len(names)):
#     my_dict[f"child{x}"] = names[x]
# print(my_dict)
#---------------loop through key and calues----------------------
# colors = {
#     "white": (255, 255, 255),
#     "grey": (128, 128, 128),
#     "red": (255, 0, 0),
#     "green": (0, 128, 0)
#     }
# for col, rgb in colors.items():
#     print(col, ":", rgb)
#-------------------loop on Keys and print values---------------------------
# d  ={}
# d['1'] = [1,2]
# d['2'] = [2,1]
# for i in d.keys():
#     print(d[i][1],end="")
#---------------------Q----------------------
# d = {'one':'two', 'three':'one','two':'three'}
# v = d['three']
# for k in range(len(d)):
#     v = d[v]
# print(v)
#--------------------------
#print(4**0.5)  #= 4 sqrt 
#----------------------------
# f = [i for i in range(-1,-2)]
# print(f)
#---------------------
# l = [[x for x in range(3)] for y in range(3)]
# for r in range(3):
#     for c in range(3):
#         if l[r][c] % 2 !=0:
#             print('#')
#-------------
# m =[1,2]
# for v in range(2):
#     m.insert(-1,m[v])
# print(m)
#---------------------
#print(1//5+1/5)
#-----------------
# x=1
# y=2
# x,y,z = x,x,y
# z,y,z = x,y,z 
# print(x,z,y)
#--------------------
# a = 1
# b=0
# a = a^b
# b=a^b
# a=a^b
# print(a,b)
#----------------
#--------------------Recursion Factorial-----------
# def factorial(x):
#         if x <0:
#             return -1
#         elif x<2:
#             return 1
#         else:
#             return x*factorial(x-1)
# print(factorial(4))
#-----------------------Prime Factors--------------
def prime_factors(x):
    factors = list()
    divisor = 2
    while(x >= divisor):
        if x%divisor == 0:
            factors.append(divisor)
            x = x/divisor
        else:
            divisor += 1
    return factors
print(prime_factors(12)) 