N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]
# [2 5 2 3 5 2 4]

# Please write your code here.
life_counts = [K for _ in range(N)]
# [5 5 5 5 5]
iterator = 0
for i in student:   # 2 5 2 3 5 2 4
    while(iterator <= M): # 0 1 2 3 4 5
        if(life_counts.count(0) == 0):
            life_counts[i - 1] -= 1
        if(iterator == M and life_counts.count(0) == 0):
            print(-1)
            break
        iterator += 1
    print(i)
    break

        