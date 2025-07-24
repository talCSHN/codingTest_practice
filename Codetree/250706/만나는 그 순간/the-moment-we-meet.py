n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.
aHistory = []
bHistory = []
aPos = 0
bPos = 0
aHistory.append(aPos)   # [0,]
bHistory.append(bPos)
for i in range(n):
    for j in range(t[i]):
        if(d[i] == 'R'):
            aPos += 1
            aHistory.append(aPos)
        elif(d[i] == 'L'):
            aPos -= 1
            aHistory.append(aPos)

for i in range(m):
    for j in range(t2[i]):
        if(d2[i] == 'R'):
            bPos += 1
            bHistory.append(bPos)
        elif(d2[i] == 'L'):
            bPos -= 1
            bHistory.append(bPos)

for i in range(1, len(aHistory)):
    if (aHistory[i] == bHistory[i]):
        print(i)
        break
    elif (i == len(aHistory) - 1):
        print(-1)


