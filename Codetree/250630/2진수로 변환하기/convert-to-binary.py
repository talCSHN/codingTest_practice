n = int(input())
digits = []

# Please write your code here.
while True:
    if (n < 2):
        digits.append(n)
        break
    
    digits.append(n % 2)
    n = n // 2

for i in digits[::-1]:
    print(i, end='')