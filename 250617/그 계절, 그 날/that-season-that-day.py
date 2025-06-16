Y, M, D = map(int, input().split())

# Please write your code here.
def isLeapYear(year):
    if (year % 4 != 0):
        return False
    elif (year % 4 == 0 and year % 100 == 0):
        return False
    elif (year % 4 == 0):
        return True
    elif (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
        return True
    else:
        return False

def isExist(year, month, day):
    if (month in range(1, 8, 2)):
        if (day <= 31):
            return True
    else:
        if (month == 2):
            if(isLeapYear(year) and day <= 29):
                return True
            elif (day <= 28):
                return True
        else:
            if (day <= 30):
                return True
    if (month == 8):
        if (day <= 31):
            return True
    elif (month in range(9, 13)):
        if (month % 2 == 0):
            if (day <= 31):
                return True
        else:
            if (day <= 30):
                return False

if (isExist(Y, M, D)):
    if (M in range(3, 6)):
        print('Spring')
    elif (M in range(6, 9)):
        print('Summer')
    elif (M in range(9, 12)):
        print('Fall')
    elif (M == 12):
        print('Winter')
    elif (M in range(1, 3)):
        print('Winter')
else:
    print(-1)