N = input()
digits = []
num = 0
# Please write your code here.
for i in range(len(N)):
    num = num * 2 + int(N[i])

num = num * 17

while True:
    if (num < 2):
        digits.append(num)
        break
    
    digits.append(num % 2)
    num = num // 2

for i in digits[::-1]:
    print(i, end='')