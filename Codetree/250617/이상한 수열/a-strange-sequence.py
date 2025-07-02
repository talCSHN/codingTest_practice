N = int(input())

# Please write your code here.
def f(n):
    if (n == 1 or n == 2):
        return n
    return f(n - 1) + f(n // 3)

print(f(N))