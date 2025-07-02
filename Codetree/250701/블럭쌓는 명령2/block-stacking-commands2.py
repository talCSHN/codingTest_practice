# 변수 선언 및 입력
n, k = tuple(map(int, input().split()))
segments = [
    tuple(map(int, input().split()))
    for _ in range(k)
]

blocks = [0] * (n + 1)

# 블럭을 특정 구간에 쌓아줍니다.
for a, b in segments:
    for i in range(a, b + 1):
        blocks[i] += 1

# 최댓값을 구합니다.
max_num = max(blocks)
print(max_num)
