def sudoku(arr):
    for i in range(9):
        if len(set(arr[i])) != 9:
            return 0
    for j in range(9):
        if len(set([arr[i][j] for i in range(9)])) != 9:
            return 0
 
    for i in range(0,9,3):
        for j in range(0,9,3):
            lst = []
            for k in range(3):
                for l in range(3):
                    lst.append(arr[i+k][j+l])
            if len(set(lst)) != 9 :
                return 0
    return 1
 
T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    ans = sudoku(arr)
    print(f"#{tc} {ans}")