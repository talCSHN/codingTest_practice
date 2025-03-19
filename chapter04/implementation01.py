# 상하좌우
x = 1
y = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n = int(input())
plans = input().split()
moveTypes = ['L', 'R', 'U', 'D']

for plan in plans:
  for i in range(len(moveTypes)):
    if plan == moveTypes[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue

  x = nx
  y = ny

print(x, y)
