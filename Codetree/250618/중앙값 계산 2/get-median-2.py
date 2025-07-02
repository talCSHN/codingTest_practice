n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(len(arr)):
    if (i % 2 == 0):
        arr[0 : i + 1] = sorted(arr[0 : i + 1])
        print(arr[(i + 1)//2], end=" ")
