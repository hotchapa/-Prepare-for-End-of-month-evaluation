def omok(arr,N,move):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == "o":
                for dir in move:
                    next_r = i
                    next_c = j
                    cnt = 0
                    while 0 <= next_r <= N-1 and 0 <= next_c <= N-1 and arr[next_r][next_c] =="o":
                        cnt += 1
                        next_r += dir[0]
                        next_c += dir[1]
                        if cnt >= 5 :
                            return "YES"
    return "NO"
 
 
 
 
 
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    move = [(-1,0),(0,-1),(1,1),(1,-1)] # 상좌 우하 좌하
    print(f"#{tc} {omok(arr,N,move)}")