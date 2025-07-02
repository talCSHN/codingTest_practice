n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
duplicate_lines = [0 for i in range(101)]

for i in range(n):
    start, end = segments[i]
    for j in range(start, end + 1):
        duplicate_lines[j - 1] += 1

print(max(duplicate_lines))