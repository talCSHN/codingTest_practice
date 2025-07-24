n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
max_cnt, cnt = 0, 0
for i in range(n):
    if (i > 0 and arr[i] > arr[i - 1]):
        cnt += 1
    else:
        cnt = 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)