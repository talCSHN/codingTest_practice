n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
i = 0
def showMax(m):
    global i
    if (len(m) == 1):
        return m[0]
    if (m[0] < max(m[1 : len(m)])):
        return showMax(m[1 : len(m)])
    else:
        return m[0]

print(showMax(arr))