# # H, W = map(int, input().split())
# # JOI = [list(input()) for _ in range(H)]
# # arr = [list([0]*W) for _ in range(H)]
# #
# # for i in range(H):
# #     for j in range(W):
# #         if JOI[i][j] == 'c' and j == 0:
# #             arr[i][j] = 0
# #             JOI[i][j+1] = 'c'
# #         if JOI[i][j] == 'c' and j >= 1:
# #             arr[i][j] = j
# #             JOI[i][j+1] = 'c'
# #         if JOI[i][j] == '.':
# #             arr[i][j] = -1
# # print(arr)
#
#
H, W = map(int, input().split())
JOI = [list(input()) for _ in range(H)]
arr = [[0] * W for _ in range(H)]

for i in range(H):
    cnt = -1
    for j in range(W):
       if JOI[i][j] == 'c':
           cnt = 0
       else:
           if cnt >= 0:
               cnt += 1
       arr[i][j] = cnt

for k in range(H):
    print(*arr[k])


# H, W = map(int, input().split())
# sky = [input() for _ in range(H)]
#
# cloud = [[0] * W for _ in range(H)]
# for i in range(H):
#     cnt = -1
#     for j in range(W):
#         if sky[i][j] == 0:
#             cloud[i][j] = 0
#             for k in range(j+1, W):
#                 if sky[i][k] == "c":
#                     break
#                 if cloud[i][k] == -1:
#                     cloud[i][k] = k - j
#
# for i in range(H):
#     for j in range(W):
#         print(cloud[i][j], end=" ")
#     print()
