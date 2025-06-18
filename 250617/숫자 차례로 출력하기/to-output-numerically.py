n = int(input())

# Please write your code here.
def orderedPrint(i):
    if (i == 0):
        return
    orderedPrint(i - 1)
    print(i, end=' ')

def reversePrint(i):
    if (i == 0):
        return
    print(i, end=' ')
    reversePrint(i - 1)

orderedPrint(n)
print()
reversePrint(n)
