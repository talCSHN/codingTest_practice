# 체스 나이트 이동 가능 경우의 수

inputData = input()
row = int(inputData[1])
column = ord(inputData[0]) - ord('a') + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
  nextRow = row + step[0]
  nextColumn = column + step[1]

  if nextRow >= 1 and nextRow <= 8 and nextColumn >=1 and nextColumn <= 8:
    result += 1

print(result)