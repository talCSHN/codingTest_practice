a, b = map(int, input().split())

# Please write your code here.
def isPrime(n):
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True

def isEven(m):
    if (((m // 10) + (m % 10)) % 2 == 0):
        return True
    else:
        return False


count = 0
for i in range(a, b + 1):
    if (isPrime(i) and isEven(i)):
        count += 1

print(count)