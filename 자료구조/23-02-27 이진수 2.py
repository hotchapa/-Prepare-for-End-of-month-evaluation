# 2진수

# N = 0.625
# 0.101 (이진수)
# = 1*(2^-1) + 0*(2^-2) + 1*(2^-3)
# = 0.5 + 0 + 0.125
# = 0.625






T = int(input())
 
for tc in range(1, T + 1):
    N = float(input())
    # N = int(N[2:])
    c_n = ''
    cnt = 0
 
    while N != 0:
        N *= 2
        if 0 < N < 1:
            c_n += '0'
        elif 1 <= N < 2:
            c_n += '1'
            N -= 1
        cnt += 1
        if cnt > 13:
            c_n = 'overflow'
            break
    print(f'#{tc} {c_n}')


