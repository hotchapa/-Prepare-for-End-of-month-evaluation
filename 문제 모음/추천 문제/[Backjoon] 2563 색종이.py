# 가로 , 세로 100
# 가로 세로 10 짜리 정사각형 검은색 색종이
N = int(input())  #색종이 개수
paper_info = [list(map(int,input().split())) for _ in range(N)] 
arr =[[0]*100 for _ in range(100)]
cnt = 0

for modi in paper_info:
    start_i = modi[1] 
    start_j = modi[0]  

    for i in range(start_i,start_i+10):
        for j in range(start_j,start_j+10):
            if 0 <= i < 100 and 0 <= j < 100 :
                arr[i][j] = 1
    
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt += 1
    
print(cnt)
