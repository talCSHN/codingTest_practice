n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
result = 0
while (m >= 1):
    if (m % 2 == 1):
        result += A[m - 1]
        m -= 1
    else:
        result += A[m - 1]
        m = int(m / 2)

print(result)