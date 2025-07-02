n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
init_arr = [0 for i in range(n)]
# print(init_arr)
max_arr = []
count1 = 0
# print(commands)
for i in range(k):
    start, end = commands[i]
    for j in range(start, end + 1):
        init_arr[j - 1] += 1
    # print(init_arr)
print(init_arr)
print(max(init_arr))
