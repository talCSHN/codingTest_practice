n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
init_arr = [0 for i in range(n+1)]
max_arr = []
count1 = 0
# print(commands)
for i in range(k):
    start, end = commands[i]
    for j in range(start, end + 1):
        init_arr[j] = 1
    max_arr.append(init_arr.count(1))
    init_arr = [0 for i in range(n)]
# print(max_arr)
print(max(max_arr))
