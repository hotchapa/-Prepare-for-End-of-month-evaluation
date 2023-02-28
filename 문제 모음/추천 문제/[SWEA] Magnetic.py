N = 1
S = 2



T = 10 # 테스트 케이스 개수 10개
for tc in range(1,T+1):
    size = int(input())
    table = [list(map(int,input().split())) for _ in range(size)] #
    result = 0
    check_list = []

    for j in range(size):
        for i in range(size):
            if table[i][j] == N or table[i][j] == S:
                check_list.append((table[i][j]))
    #
    for k in range(len(check_list)-1):
        if check_list[k] == N and check_list[k+1] == S:
            result += 1

    print(f"#{tc} {result}")
    

# 코드를 수정해보겠습니다.

# 문제에서는 테이블의 크기가 항상 100x100이라고 했으므로, 테이블의 크기를 미리 100으로 고정시킬 수 있습니다. 또한, 자성체는 가장자리에 있을 수 없으므로, 이를 고려하여 테이블 크기를 102x102로 만들고, 테이블의 경계에 0을 추가합니다.

# 그리고 자성체의 방향에 따라서 검사해야 하는 방향이 달라지므로, N 극인 경우에는 아래쪽으로, S 극인 경우에는 오른쪽으로만 검사하면 됩니다.

# 다음은 수정된 코드입니다.

T = 10

for tc in range(1, T+1):
    size = int(input())
    table = [[0] * 102 for _ in range(102)]
    for i in range(1, 101):
        row = list(map(int, input().split()))
        for j in range(1, 101):
            table[i][j] = row[j-1]

    count = 0
    for i in range(1, 101):
        for j in range(1, 101):
            if table[i][j] == 1:
                x, y = i+1, j
                while table[x][y] == 0:
                    x += 1
                if table[x][y] == 2:
                    count += 1

            elif table[i][j] == 2:
                x, y = i, j+1
                while table[x][y] == 0:
                    y += 1
                if table[x][y] == 1:
                    count += 1

    print(f"#{tc} {count}")



