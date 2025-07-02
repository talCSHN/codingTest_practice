n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

# Please write your code here.
class Point:
    def __init__(self, idx, x, y):
        self.idx = idx
        self.x = x
        self.y = y
    def __str__(self):
        return f'{self.idx}'

pointObjs = [Point(points[i][0], points[i][1][0], points[i][1][1]) for i in range(n)]
for i in range(n):
    if (pointObjs[i].x < 0):
        pointObjs[i].x = pointObjs[i].x * -1
    if (pointObjs[i].y < 0):
        pointObjs[i].y = pointObjs[i].y * -1

distances = [(pointObjs[i].idx + 1, pointObjs[i].x + pointObjs[i].y) for i in range(n)]
distances.sort(key= lambda x: (x[1], x[0]))
for i in range(n):
    print(f'{distances[i][0]}')