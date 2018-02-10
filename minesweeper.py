def  solve_minesweeper(puzzle_array):
    x = [[0 for i in range(len(puzzle_array))] for j in range(len(puzzle_array))]
    #Rule 1
    le = len(puzzle_array)
    
    for i in range(le):
        for j in range(le):
            c=0
            for k in range(-1,2):
                for l in range(-1,2):
                    if(i+k<0 or i+k>= le or j+l<0 or j+l>= le or (k==0 and l==0)):
                        continue
                    if(puzzle_array[i+k][j+l] == 'm'):
                        c+=1
            x[i][j] = c;

    for i in range(1, le):
        for j in range(le):
            if(puzzle_array[i-1][j] == 'm'):
                        x[i][j] = 2;
    
    for i in range(le):
        for j in range(1, le):
            if(puzzle_array[i][j-1] == 'm'):
                        x[i][j] = 0;
    for i in range(le):
        if(i%2==0):
            continue
        ismine = 0
        for j in range(le):
            if(puzzle_array[i][j] == 'm'):
                        ismine = 1
                        break
        if ismine == 1:
            for j in range(le):
                x[i][j] *=3

    for i in range(le):
        for j in range(le):
            c=0
            for k in range(-1,2):
                for l in range(-1,2):
                    if(i+k<0 or i+k>= le or j+l<0 or j+l>= le or k==0 or l==0 ):
                        continue
                    if(puzzle_array[i+k][j+l] == 'm'):
                        c=1
                        break
            if c ==1:
                x[i][j] *=2
    for i in range(le):
        for j in range(le):
            if(puzzle_array[i][j] == 'm'):
                x[i][j] = -1
    return x

y = [['.','m','.','.'],['.','.','.','.'],['.','.','.','m'],['m','.','.','.']]
print solve_minesweeper(y)