a, b, c, d = map(int, input().split())

# Please write your code here.
elapsed_time = 0

while True:
    if a == c and b == d:
        break

    elapsed_time += 1
    b += 1

    if b == 60:
        a += 1
        b = 0

print(elapsed_time)
