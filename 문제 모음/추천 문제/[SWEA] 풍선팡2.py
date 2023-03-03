def pang(starti,startj):
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    score = 0
    score += arr[starti][startj]
 
    for dir in move:
        nexti = starti + dir[0]
        nextj = startj + dir[1]
        if 0 <= nexti < N and 0<= nextj < M:
            score += arr[nexti][nextj]
 
    return score
 
T = int(input())
 
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    starti = 0
    startj = 0
 
    maxscore = pang(starti,startj)
    for i in range(N):
        for j in range(M):
            score = pang(i,j)
            if maxscore < score :
                maxscore = score
 
    print(f"#{tc} {maxscore}")