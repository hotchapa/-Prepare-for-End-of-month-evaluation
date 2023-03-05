t = int(input())

for tc in range(1, t + 1):
    words = [list(input()) for _ in range(5)]
    ans = ''
    for j in range(15):
        for i in range(5):
            if len(words[i]) > j:
                ans += words[i][j]

    print(f'#{tc}', ans)

t = int(input())

for idx in range(1, t + 1):
    print('#{}'.format(idx), end=' ')

    # 다섯개의 단어들 받아오기
    words = []
    for _ in range(5):
        words.append(list(input()))

    # 세로로 읽기
    for i in range(15):
        for j in range(5):
            # try except을 이용해서 인덱스 에러 안나도록 해줌.
            try:
                print(words[j][i], end='')
            except:
                continue