N = 1
S = 2



T = 10 
for tc in range(1,T+1):
    size = int(input())
    table = [list(map(int,input().split())) for _ in range(size)] #
    result = 0


    for j in range(size):
        check_list = []
        for i in range(size):
            if table[i][j] == N or table[i][j] == S:
                check_list.append((table[i][j]))
    
        for k in range(len(check_list)-1):
            if check_list[k] == N and check_list[k+1] == S:
                result += 1

    print(f"#{tc} {result}")


# 코드를 수정해보겠습니다.

# 문제에서는 테이블의 크기가 항상 100x100이라고 했으므로, 테이블의 크기를 미리 100으로 고정시킬 수 있습니다. 또한, 자성체는 가장자리에 있을 수 없으므로, 
# 이를 고려하여 테이블 크기를 102x102로 만들고, 테이블의 경계에 0을 추가합니다.

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




T = 10
for tc in range(1,T+1):
    size = int(input())
    table = [list(map(int,input().split())) for _ in range(size)]
    count = 0

    for j in range(size):
        pole = 0
        for i in range(size):
            if table[i][j] == 1:  # N극인 경우
                if pole == 2:  # 이전에 S극이 나왔던 경우
                    count += 1
                pole = 1
            elif table[i][j] == 2:  # S극인 경우
                if pole == 1:  # 이전에 N극이 나왔던 경우
                    count += 1
                pole = 2

    print(f"#{tc} {count}")




N = 1
S = 2

T = 10
for tc in range(1,T+1):
    size = int(input())
    table = [list(map(int,input().split())) for _ in range(size)]
    result = 0
    check_list = []

    for j in range(size):
        for i in range(size):
            if table[i][j] == N or table[i][j] == S:
                check_list.append((j, table[i][j]))

    for k in range(len(check_list)-1):
        if check_list[k][1] == N and check_list[k+1][1] == S:
            result += 1

    print(f"#{tc} {result}")



N = 1
S = 2

T = 10 # 테스트 케이스 개수 10개

for tc in range(1,T+1):
    size = int(input())
    table = [list(map(int,input().split())) for _ in range(size)]
    result = 0

    for j in range(size):
        check_list = []
        for i in range(size):
            if table[i][j] != 0:
                check_list.append(table[i][j])

        if len(check_list) >= 2:
            if check_list[0] == N and check_list[-1] == S:
                result += 1
            for k in range(len(check_list)-1):
                if check_list[k] == S and check_list[k+1] == N:
                    result += 1

    print(f"#{tc} {result}")





T = int(input())  # 테스트 케이스 개수 입력

for tc in range(1, T+1):
    N = int(input())  # 표의 크기
    table = [list(map(int, input().split())) for _ in range(N)]  # 표 입력
    cnt = 0  # 결과값

    # 모든 열에 대해 탐색
    for j in range(N):
        flag = 0  # flag 변수 초기화
        for i in range(N):
            if table[i][j] == 1:  # N극인 경우
                flag = 1
            elif table[i][j] == 2:  # S극인 경우
                if flag == 1:  # 이전에 N극이 나왔었다면
                    cnt += 1  # 조건 만족, 결과값 증가
                    flag = 2  # flag 값을 2로 변경
            else:  # 0인 경우
                continue

    print(f"#{tc} {cnt}")  # 결과 출력



# 문제에서는 테이블의 크기가 항상 100x100이라고 했으므로, 
# 테이블의 크기를 미리 100으로 고정시킬 수 있습니다. 
# 또한, 자성체는 가장자리에 있을 수 없으므로, 
# 이를 고려하여 테이블 크기를 102x102로 만들고, 
# 테이블의 경계에 0을 추가합니다.

# 그리고 자성체의 방향에 따라서 검사해야 하는 방향이 달라지므로, N 극인 경우에는 아래쪽으로, S 극인 경우에는 위쪽으로만 검사하면 됩니다.
# 다음은 수정된 코드입니다.



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
    for k in range(len(check_list)-1):
        if check_list[k] == N and check_list[k+1] == S:
            result += 1
        

    print(f"#{tc} {result}")
