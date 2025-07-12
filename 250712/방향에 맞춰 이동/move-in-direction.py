n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
# (N, 3) (E, 2) (S, 1) (E, 2)
# dir = [N, E, S, E]
# dist = [3, 2, 1, 2]
# (E, N, W, S)
dx = [1, 0, -1, 0] # 동 북 서 남
dy = [0, 1, 0, -1] # 동 북 서 남
nx, ny = 0, 0
E, N, W, S = 0, 1, 2, 3

def move(direction, num):
    global nx, ny
    if (direction == 'E'):
        nx = nx + (dx[E] * num)
        ny = ny + (dy[E] * num)
    elif (direction == 'N'):
        nx = nx + (dx[N] * num)
        ny = ny + (dy[N] * num)
    elif (direction == 'W'):
        nx = nx + (dx[W] * num)
        ny = ny + (dy[W] * num)
    elif (direction == 'S'):
        nx = nx + (dx[S] * num)
        ny = ny + (dy[S] * num)

for i in range(n):
    move(dir[i], dist[i])

print(f'{nx} {ny}')