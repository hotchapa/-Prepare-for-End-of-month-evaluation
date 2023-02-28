N = 1
S = 2



T = 10 # 테스트 케이스 개수 10개
for tc in range(1,T+1):
    size = int(input())
    table = [list(map(int,input().split())) for _ in range(100)] #
    result = 0
    check_list = []

    for j in range(size):
        for i in range(size):
            if table[i][j] == N or table[i][j] == S:
                check_list.append((table[i][j]))
    #
    for k in range(len(check_list)):
        if check_list[k] == N and check_list[k+1] == S:
            result += 1

    print(f"#{tc} {result}")


