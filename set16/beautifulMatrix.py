matrix = []
for i in range(5):
    line = list(map(int,input().split()))
    matrix.append(line)
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            rowGap = abs(3 - (i+1))
            columnGap = abs(3 - (j+1)) 
            print(abs(rowGap + columnGap))
            break