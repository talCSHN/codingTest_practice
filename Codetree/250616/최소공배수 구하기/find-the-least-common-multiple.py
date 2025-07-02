n, m = map(int, input().split())

# Please write your code here.
dList = []
mList = []

def makeDivisor(a ,b):
    for i in range(1, min(a, b) + 1):
        if (a % i == 0 and b % i == 0):
            dList.append(i)
    return max(dList)


def makeMultiple(a, b):
    divisor = makeDivisor(a, b)
    dOfA = int(a / divisor)
    dOfB = int(b / divisor)
    print(divisor * dOfA * dOfB) 

makeMultiple(n, m)
