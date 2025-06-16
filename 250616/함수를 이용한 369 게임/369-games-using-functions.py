a, b = map(int, input().split())

# Please write your code here.
def is369(n):
    if (n//10 == 3 or n//10 == 6 or n//10 == 9 or n%10 == 3 or n%10 == 6 or n%10 == 9):
        return True
    else:
        return False

def is3Multiple(n):
    if (n % 3 == 0):
        return True
    else:
        return False


count = 0
for i in range(a, b + 1):
    if (is369(i) or is3Multiple(i)):
        count += 1

print(count)