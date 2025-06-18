n = int(input())

# Please write your code here.
def printStar(i):
    if (i == 0):
        return
    printStar(i - 1)
    print('*' * i)

printStar(n)