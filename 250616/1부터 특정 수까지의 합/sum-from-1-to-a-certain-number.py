n = int(input())

# Please write your code here.
sumResult = 0
def returnSum(m):
    global sumResult
    for i in range(1, m + 1):
        sumResult += i
    sumResult //= 10
    return sumResult

answer = returnSum(n)
print(answer)