a, b = map(int, input().split())
n = input()
answer = []
# Please write your code here.
num = 0
for i in range(len(n)):
    num = num * a + int(n[i])

while True:
    if (num < b):
        answer.append(num)
        break
    
    answer.append(num % b)
    num = num // b

for i in answer[::-1]:
    print(i, end='')