n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
duplicate_segment = [0 for i in range(200)]
for i in range(n):
    if (segments[i][0] < 0 or segments[i][1] < 0):
        start = segments[i][0] + (min(segments[i]) * -1)
        end = segments[i][1] + (min(segments[i]) * -1)
    else:
        start, end = segments[i]
    for j in range(start, end):
        duplicate_segment[j] += 1

print(max(duplicate_segment))
