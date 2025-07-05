n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
OFFSET = 100
init_matrix = [[0]*201 for _ in range(201)]
## x = [0, 4, 0]
## y = [0, 0, 4]

for i in range(n):
    x[i] = x[i] + OFFSET
    y[i] = y[i] + OFFSET
    for j in range(x[i], x[i] + 8):
        for k in range(y[i], y[i] + 8):
            init_matrix[j][k] = 1

# width = init_matrix.count(1)
width = 0
for i in range(201):
    for j in range(201):
        if (init_matrix[i][j] == 1):
            width += 1
print(width)
