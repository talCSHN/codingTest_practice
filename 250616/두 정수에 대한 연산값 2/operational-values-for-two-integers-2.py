a, b = map(int, input().split())

# Please write your code here.
def calculate(m, n):
    if (m > n):
        m *= 2
        n += 10
    elif (m < n):
        m += 10
        n *= 2
    print(m , n)

calculate(a, b)