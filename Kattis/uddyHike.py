dim_x = [1, -1, 0, 0]
dim_y = [0, 0, 1, -1]

n_rows, n_columns = input().split()
n_rows, n_columns = int( n_rows), int(n_columns) # 2,2
log_matrix = [[-1 for x in range(n_columns + 2)] for y in range(n_rows)]   #[[-1, -1, -1, -1], [-1, -1, -1, -1]]

for i in range(n_rows):
    g=input().split()
    for j in range(1, n_columns + 1):
        log_matrix[i][j] = int(g[j-1])  #[[-1,3,0,-1],[-1,1,2,-1]]

mud_matrix = [[1000001 for x in range(n_columns + 2)] for y in range(n_rows)]   #matrix with 100001 value
mud_matrix[0][0] = 0   # give a start value
result = [(0, 0, 0)]   #tuple  0,x,y

while len(result) > 0:
    current_x = result[0][1]
    current_y = result[0][2]
    del result[0]

    for i in range(4):       # check the 4_dimension value
        next_x = current_x + dim_x[i]
        next_y = current_y + dim_y[i]
        # next_x within the row numbers, next_y within the column numbers,
        if ((next_x >= 0) and next_x < n_rows) and ((next_y >= 0) and next_y < n_columns + 2):
            next_val = max(mud_matrix[current_x][current_y], log_matrix[next_x][next_y])    # max(0,-1) = 0
            if next_val < (mud_matrix[next_x][next_y]):
                mud_matrix[next_x][next_y] = next_val
                result.append((next_val, next_x, next_y))   # 0, 1, 0
                result.sort()

print(mud_matrix[0][n_columns + 1])