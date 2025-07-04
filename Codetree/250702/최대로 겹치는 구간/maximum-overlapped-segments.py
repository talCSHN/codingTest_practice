n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
OFFSET = 100
duplicate_segment = [0 for i in range(202)]
for start, end in segments:
    start += OFFSET
    end += OFFSET
    for j in range(start, end):
        duplicate_segment[j] += 1

print(max(duplicate_segment))
