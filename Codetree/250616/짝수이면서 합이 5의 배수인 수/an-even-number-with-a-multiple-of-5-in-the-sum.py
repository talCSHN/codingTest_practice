n = int(input())

# Please write your code here.
def isFiveMultiple(m):
    if (n % 2 == 0 and (n // 10 + n % 10) % 5 == 0):
        return True
    else:
        return False


if (isFiveMultiple(n)):
    print('Yes')
else:
    print('No')