import random

totalLotto = []
lotto = []
pickNum = 0
count = 0

print('로또 번호 자동 생성기')
count = int(input('몇 장 드릴까요?'))

for _ in range(count):
    lotto = []
    while True:
        pickNum = random.randint(1, 45)
        if pickNum not in lotto:
            lotto.append(pickNum)
        if len(lotto) > 6:
            break
    totalLotto.append(lotto)

for lotto in totalLotto:
    lotto.sort()
    print('자동 번호 : ', end= ' ')
    for i in range(0, 6):
        print(f'{lotto[i] : 2d}', end= ' ')

    print()