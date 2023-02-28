# 2진수
T = int(input())

# 10 이 넘는 숫자를 위한 변환기
converter = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

for tc in range(1, T+1):
    N, number = input().split()
    # 최종 값 초기화
    result = ''
    # 읽는거는 뒤에서 부터 읽어오자
    for n in number[::-1]:
        # 변환기 안에 있는 숫자라면 변환해주자
        if n in converter:
            n = converter[n]
        # 변환기 안에 없는 숫자는 str로 들어오기 때문에 변환해주기
        n = int(n)
        # 16진수는 무조건 4자리 차지하니 4번 반복해준다.
        for _ in range(4):
            result = str(n % 2) + result
            n //= 2

    print(f"#{tc} {result}")