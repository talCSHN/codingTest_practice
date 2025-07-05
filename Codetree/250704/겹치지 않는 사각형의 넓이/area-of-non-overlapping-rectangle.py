x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
OFFSET = 1000

init_matrix = [[0]*2001 for i in range(2001)]

rectangles = [[x1[i], y1[i], x2[i], y2[i]] for i in range(3)]

for x1, y1, x2, y2 in rectangles[0:2]:
    x1 = x1 + OFFSET
    y1 = y1 + OFFSET
    x2 = x2 + OFFSET
    y2 = y2 + OFFSET

    for x in range(x1, x2):
        for y in range(y1, y2):
            init_matrix[x][y] = 1

    for x in range(rectangles[2][0] + OFFSET, rectangles[2][2] + OFFSET):
        for y in range(rectangles[2][1] + OFFSET, rectangles[2][3] + OFFSET):
            init_matrix[x][y] -= 1

width = 0
for x in range(0, 2001):
    for y in range(0, 2001):
        if (init_matrix[x][y] == 1):
            width += 1

print(width)


            
