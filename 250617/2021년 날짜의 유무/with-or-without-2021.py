M, D = map(int, input().split())

# Please write your code here.

dateList = []
for i in range(1, 13):
    for j in range(1, 32):
        if (i % 2 == 1 or i == 8):
            dateList.append((i, j))
        elif (i == 2 and j < 28):
            dateList.append((i, j))
            if (j == 28):
                dateList.append((i, j))
                break
        else:
            if (j < 31):
                dateList.append((i, j))
            else:
                break

def isIn2021(a, b):
    if ((a, b) in dateList):
        print('Yes')
    else:
        print('No')

isIn2021(M, D)