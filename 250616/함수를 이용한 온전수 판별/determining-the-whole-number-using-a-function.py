a, b = map(int, input().split())

# Please write your code here.
def isPerfect(n):
    if (n % 2 == 0):
        return False
    elif (n % 10 == 5):
        return False
    elif (n % 3 == 0 and n % 9 != 0):
        return False
    return True

count = 0
for i in range(a, b + 1):
    if (isPerfect(i)):
        count += 1

print(count)