N = int(input())

# Please write your code here.
def printRecursive(i):
    if (i == 0):
        return
    print(i, end=" ")
    printRecursive(i - 1)
    print(i, end=" ")

printRecursive(N)