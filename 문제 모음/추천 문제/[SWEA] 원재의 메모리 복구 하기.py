T = int(input())
for tc in range(1, T + 1):
    m = input()
 
    memory = "0"
    cnt = 0
    for i in range(len(m)):
        if m[i]!= memory :
            memory = m[i]
            cnt +=1
 
    print(f"#{tc} {cnt}")