OFFSET = 100

n = int(input())
rectangles = [tuple(map(int, input().split())) for _ in range(n)]

init_matrix = [[0]*201 for _ in range(201)]

for x1, y1, x2, y2 in rectangles:
    x1 = x1 + OFFSET
    y1 = y1 + OFFSET
    x2 = x2 + OFFSET
    y2 = y2 + OFFSET
    
    for x in range(x1, x2):
        for y in range(y1, y2):
            init_matrix[x][y] = 1

width = 0
for x in range(0, 201):
    for y in range(0, 201):
        if (init_matrix[x][y] > 0):
            width += 1

print(width)
    