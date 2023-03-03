def isAllStartsInCam(centerI, centerJ, k): # 센터 기준으로 별이다 찍혔는지 확인
    global isPossible

    # 센터를 기준으로 시작점, 끝점 지정
    startI = centerI - k//2
    endI = centerI + k//2
    startJ = centerJ - k//2
    endJ = centerJ + k//2
    starCnt = 0 # 센 별 수
    for i in range(startI, endI+1):
        for j in range(startJ, endJ+1):

            if i >= N or j >= N: # 인덱스 벗어나면 불가능한 것
                isPossible = False
                return

            if sky[i][j] == '*': # 별 세기
                starCnt += 1

    if starCnt == totalStarCnt: # 별을 다 담았으면 True리턴
        return True

T = int(input())
for test_case in range(1,T+1):
    N, K, A, B = map(int, input().split())
    sky = [input().split() for _ in range(N)]

    totalStarCnt = 0
    for i in range(N):
        for j in range(N):
            if sky[i][j] == '*':
                totalStarCnt +=1

    isPossible = True # 가능여부

    gap = 0 # 캠크기
    for k in range(1, K+1, 2):
        if isAllStartsInCam(A,B,k):
            gap = k # 작은 캠 크기부터 시작해서 담을 수 있다면 해당 캠크기 적용 후 break
            break

    else: # 반복문 다돌아도 한번도 break없이 다 사진찍기 실패했다면
        isPossible = False

    ans = (K - gap)//2 if isPossible else -1 # 가능하다면 몇번 확대했는지, 불가능하다면 -1
        
    print(f'#{test_case} {ans}')