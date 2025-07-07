N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]
# [2 5 2 3 5 2 4]

# Please write your code here.
life_counts = [K for _ in range(N)]
# [5 5 5 5 5]
is_exits = False

for i in student:   # 2 5 2 3 5 2 4
    life_counts[i - 1] -= 1
    if(life_counts[i - 1] == 0):
        is_exits = True
        print(i)
        break

if (is_exits == False):
    print(-1)
        