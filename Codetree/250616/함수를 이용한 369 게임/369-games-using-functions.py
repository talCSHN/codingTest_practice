a, b = map(int, input().split())

# Please write your code here.
def is369(n):
    n = str(n)
    if (('3' in n) or ('6' in n) or ('9' in n)):
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