x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
## x1[0,0] y1[0,0] x2[0,0] y2[0,0]
OFFSET = 1000
rectangles = [[x1[i], y1[i], x2[i], y2[i]] for i in range(2)]
init_width = [[0]*2001 for _ in range(2001)]
for a1, b1, a2, b2 in rectangles:
    a1 = a1 + OFFSET
    b1 = b1 + OFFSET
    a2 = a2 + OFFSET
    b2 = b2 + OFFSET
    if (a1 == x1[0]+OFFSET):
        for x in range(a1, a2):
            for y in range(b1, b2):
                init_width[x][y] = 1
    else:
        for x in range(a1, a2):
            for y in range(b1, b2):
                init_width[x][y] = 0

xArr = []
yArr = []
for x in range(2001):
    for y in range(2001):
        if(init_width[x][y] == 1):
            xArr.append(x)
            yArr.append(y)
# xArr.sort()
# yArr.sort()
coverWidth = (max(xArr) - min(xArr) + 1) * (max(yArr) - min(yArr) + 1)
print(coverWidth)
# print(xArr)
# print(yArr)