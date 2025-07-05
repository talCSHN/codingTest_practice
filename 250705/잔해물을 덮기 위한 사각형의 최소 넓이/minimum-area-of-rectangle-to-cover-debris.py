x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
## x1[0,0] y1[0,0] x2[0,0] y2[0,0]
OFFSET = 1000
rectangles = [[x1[i], y1[i], x2[i], y2[i]] for i in range(2)]
init_width = [[0]*2001 for _ in range(2001)]
for x11, y11, x22, y22 in rectangles:
    x11 = x11 + OFFSET
    y11 = y11 + OFFSET
    x22 = x22 + OFFSET
    y22 = y22 + OFFSET
    for x in range(x1[0], x2[0]):
        for y in range(y1[0], y2[0]):
            init_width[x][y] = 1
    for x in range(x1[1], x2[1]):
        for y in range(y1[1], y2[1]):
            init_width[x][y] = 0
xArr = []
yArr = []
for x in range(2001):
    for y in range(2001):
        if(init_width[x][y] == 1):
            xArr.append(x)
            yArr.append(y)

coverWidth = (max(xArr) - min(xArr) + 1) * (max(yArr) - min(yArr) + 1)
print(coverWidth)
