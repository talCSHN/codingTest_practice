n, m = map(int, input().split())

# Please write your code here.
list = []
def showDivisor(a, b):
    for i in range(1, min(a, b) + 1):
        if (a % i == 0 and b % i == 0):
            list.append(i)
    print(max(list))

showDivisor(n, m)