N = int(input())

# Please write your code here.
def f(n):
    if (n == 1):
        return 1
    elif (n == 2):
        return 2

    return n + f(n - 2)

print(f(N))
    