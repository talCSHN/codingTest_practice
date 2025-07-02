n = int(input())

# Please write your code here.
count = 0
def f(n):
    global count
    if (n == 1):
        return count

    if (n % 2 == 0):
        count += 1
        return f(n // 2)
    else:
        count += 1
        return f(n * 3 + 1)

print(f(n))