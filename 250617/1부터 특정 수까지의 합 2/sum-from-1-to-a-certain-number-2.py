N = int(input())

# Please write your code here.
def returnSum(n):
    if (n == 1):
        return 1
    return n + returnSum(n - 1)

print(returnSum(N))