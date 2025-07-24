N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
max_cnt, cnt = 0, 0
plus_minus_arr = []
for num in arr:
    if(num > 0):
        plus_minus_arr.append(1)
    if(num < 0):
        plus_minus_arr.append(0)
for i in range(N):
    if (i > 0 and plus_minus_arr[i] == plus_minus_arr[i - 1]):
        cnt += 1
    else:
        cnt = 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)