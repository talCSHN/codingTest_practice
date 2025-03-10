# 숙지할 것
# list(map(int, input().split()))
# 동작 속도 빠른 입력
# import sys
# data = sys.stdin.readline().rstrip()
# print(data)

# 큰 수의 법칙
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count1 = (m // (k + 1)) * k  # first가 등장하는 총 횟수 (k번씩 반복되는 블록 개수)
count1 += m % (k + 1)        # 나머지에서 first가 등장하는 횟수

count2 = m - count1          # second가 등장하는 총 횟수

result = count1 * first + count2 * second


print(result)
