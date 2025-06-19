# 동전 거슬러주기
# n = int(input('돈 입력 '))
n = 1260
count = 0

coinTypes = [500, 100, 50, 10]
for coin in coinTypes:
    count += n // coin # 몫 2/ 260//100 = 2/ 60//50 = 1/ 10//10 = 1
    n %= coin # 260/ 260%100 = 60/ 60%50 = 10/ 10%10 = 0

print(count) # 6