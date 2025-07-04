n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
# x -> [2, 6, 1 ...]
# di-> [R, L, R]
visit_history = [0 for i in range(2002)]
curr_pos = 1001
for i in range(n):
    if (dir[i] == 'R'):
        for j in range(curr_pos, curr_pos + x[i]):
            visit_history[j] += 1
        curr_pos = curr_pos + x[i]
    elif (dir[i] == 'L'):
        for k in range(curr_pos - x[i], curr_pos):
            visit_history[k] += 1
        curr_pos = curr_pos - x[i]

duplicate_count = 0
for i in range(len(visit_history)):
    if (visit_history[i] >= 2):
        duplicate_count += 1

print(duplicate_count)
    