N = int(input())

# Please write your code here.
def returnSum(i):
    if (i < 10):
        return i * i
    return returnSum(i // 10) + (i % 10) * (i % 10)

print(returnSum(N))