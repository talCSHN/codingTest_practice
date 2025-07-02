n = int(input())

# Please write your code here.
def makeSquareNum(m):
    num = 0
    for i in range(m):
        for j in range(m):
            print((num % 9) + 1  , end=' ')
            num += 1
        print()

makeSquareNum(n)
