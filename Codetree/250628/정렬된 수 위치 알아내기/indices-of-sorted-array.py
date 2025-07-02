n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.

sequences = []
for idx, value in enumerate(sequence):
    sequences.append((idx, value))

sequences.sort(key= lambda x: (x[1], x[0]))

answers = []
for idx, value in enumerate(sequences):
    answers.append((idx + 1, value))

answers.sort(key= lambda x: x[1][0])

for i in range(n):
    print(answers[i][0], end=' ')