y = int(input())

# Please write your code here.

def isLeapYear(n):
    if (n % 4 != 0):
        return False
    elif (n % 100 == 0 and n % 400 != 0):
        return False
    else:
        return True

if (isLeapYear(y)):
    print('true')
else:
    print('false')