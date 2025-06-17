n = int(input())

# Please write your code here.
def printStr(m):
    global n
    if (m == 0):
        return
    printStr(m - 1)
    print('HelloWorld')

printStr(n)