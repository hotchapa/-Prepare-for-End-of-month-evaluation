T = int(input())
for test_case in range(1,T+1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    totalCost = 0
    treeCnt = 0
    mostExpensiveTreePrice = grid[0][0]
    colOfMostExpensiveTreePrice = 0

    for i in range(N):
        for j in range(0, M, 2):
            treePrice = grid[i][j]
            totalCost += treePrice
            treeCnt +=1
            if mostExpensiveTreePrice <= treePrice:
                mostExpensiveTreePrice = treePrice
                colOfMostExpensiveTreePrice = j+1

    print(f'#{test_case} {totalCost} {treeCnt} {mostExpensiveTreePrice} {colOfMostExpensiveTreePrice}')