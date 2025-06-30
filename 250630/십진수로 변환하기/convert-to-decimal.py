binary = input()
binary_int = [int(i) for i in binary]
num = 0
# Please write your code here.
for i in range(len(binary_int)):
    num = num * 2 + binary_int[i]

print(num)