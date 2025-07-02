n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def isSequence(n, m):
    for i in range(len(n) - len(m) + 1):
        if (m == n[i : i + len(m)]):
            return True
    return False

if (isSequence(a, b)):
    print('Yes')
else:
    print('No')