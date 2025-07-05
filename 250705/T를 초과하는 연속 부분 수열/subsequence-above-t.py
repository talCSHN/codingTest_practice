n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
max_cnt, cnt = 0, 0
for i in range(n):
    if(i > 0 and arr[i] > t and arr[i - 1] > t):
        cnt += 1
    elif (arr[i] > t):
        cnt = 1
    else:
        cnt = 0
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)