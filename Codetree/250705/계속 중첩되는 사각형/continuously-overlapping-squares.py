n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
# x1[2, 5] y1[1, -1] x2[7, 10] y2[4, 3]
OFFSET = 100
rectangles = [[x1[i], y1[i], x2[i], y2[i]] for i in range(n)]
init_matrix = [[0]*201 for _ in range(201)]
change_turn = True
for a1, b1, a2, b2 in rectangles:
    a1 = a1 + OFFSET
    b1 = b1 + OFFSET
    a2 = a2 + OFFSET
    b2 = b2 + OFFSET
    for x in range(a1, a2):
        for y in range(b1, b2):
            if (change_turn):
                init_matrix[x][y] = 1
            else:
                init_matrix[x][y] = 2
    if(change_turn):
        change_turn = False
    else:
        change_turn = True

## 1 -> red / 2 -> blue
blue_count = 0
for i in range(201):
    for j in range(201):
        if(init_matrix[i][j] == 2):
            blue_count += 1

print(blue_count)

