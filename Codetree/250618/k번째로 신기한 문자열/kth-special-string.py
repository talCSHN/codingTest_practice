n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
list = []
for i in str:
    if (i[0:len(t)] == t):
        list.append(i)
list.sort()
print(list[k - 1])