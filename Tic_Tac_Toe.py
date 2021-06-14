# import sys, random, time

# def turn(board, board2, pos1):
#     for i in range(len(board2)):
#         for n in range(len(board2[i])):
#             if board2[i][n] == str(pos1):
#                 board2[i][n] = logo
#                 board[i][n] = logo
#     for i in board:
#         print("|".join(i))
#     return board, board2, pos1

# def PcPlay(board, board2, pos1):
#     numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]       
#     numbers = list(set(numbers) - set(taken))        
#     pos1 = "".join(random.choice(numbers))        
#     if pos1 not in taken:
#         print()
#         print('Pc thinking...')
#         time.sleep(2)
#         print("Pc made it's move: " + pos1)
#         taken.append(pos1)
#         board, board2, pos1 = turn(board, board2, pos1)
#         return board, board2, taken

# def winGame(board2):
#     for i in range(3):    
#         if "XXX" == str("".join(board2[i][0:3])) or "XXX" ==(board2[0][i] + board2[1][i] + board2[2][i]) or (
#                 board2[0][0] + board2[1][1] + board2[2][2]) == "XXX" or (
#                 board2[0][2] + board2[1][1] + board2[2][0]) == "XXX":
#             print('\x1b[93;79;46m' + ' You win! ' + '\x1b[0m')
#             sys.exit()
            
#     for i in range(3):  
#         if "OOO" == str("".join(board2[i][0:3])) or "OOO" ==(board2[0][i] + board2[1][i] + board2[2][i]) or (
#                 board2[0][0] + board2[1][1] + board2[2][2]) == "OOO" or (
#                 board2[0][2] + board2[1][1] + board2[2][0]) == "OOO":
#             print('\x1b[7;37;46m' + ' You Lose!!! ' + '\x1b[0m')
#             sys.exit()    

# board  = [["_", "_", "_"], 
#           ["_", "_", "_"], 
#           ["_", "_", "_"]]
# board2 = [["7", "8", "9"], 
#           ["4", "5", "6"], 
#           ["1", "2", "3"]]
# taken  = []

# print('\n\t ..: Welcome to Tic Tac Toe :..')
# print('Choose a number from the Keypad:')
# print('7|8|9\n4|5|6\n1|2|3')

# game = True
# move = 0
# while game:
#     logo = 'X'
#     p1 = True

#     while p1:
#         pos1 = input('>Player: ')
#         board, board2, pos1 = turn(board, board2, pos1)
#         if pos1 not in taken:
#             taken.append(pos1)
#             p1 = False
#     if pos1 not in taken:
#         move += 1        
  
#     winGame(board2)
#     move += 1
#     if move == 9:
#         print('\x1b[7;36;47 m' + ' nobody wins! ' + '\x1b[0m')
       
#         game = False
#         sys.exit()
#     logo = 'O'
#     PcPlay(board,board2,pos1)
#     winGame(board2)
#     move += 1 
#-------------------------chess sqr color-------------------------------------------
square = input('Enter a chess square identifier (e.g. e5): ')
# ord() returns the Unicode code point.  The code point for 'a' is 97,'b' is 98
if (ord(square[0]) + int(square[1])) % 2:
    print(f'\n{square} is White', end='')
else:
    print(f'\n{square} is Black', end='')
# #----------------------------tic tac toe-----------------------------------
# X = 3
# Y = 3

# current_position = [' ' for _ in range(X * Y + 1)]
# player = 'X'
# while True:
#     for i in range(X*Y - X + 1, 0, -X):
#         for j in range(X):
#             print(current_position[i + j], end='')
#             if (i + j) % X:
#                 print('|', end='')
#         print()
#         if i > X:
#             for j in range(X):
#                 print('-', end='')
#                 if (i + j) % X:
#                     print('+', end='')
#             print()
#     move = int(input(f"It's your turn,{player}.Move to which place?\n"))
#     current_position[move] = player
#     player = '0' if player == 'X' else 'X'   
