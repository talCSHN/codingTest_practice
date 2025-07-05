n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
cnt = 0
cnt_arr = []
is_block = False
idx = 0
for i in range(n):
    if(arr[i] == 0 or arr[i] != arr[i - 1]):
        is_block = True
        cnt += 1
    if(is_block and arr[i] == arr[i - 1]):
        idx = i
        cnt = 0
        while (idx < n - 1 and arr[i] == arr[i - 1]):
            cnt += 1
            idx += 1

print(cnt)

    