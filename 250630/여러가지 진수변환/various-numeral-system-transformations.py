N, B = map(int, input().split())
answer = []
# Please write your code here.
while True:
    if N < B:
        answer.append (N)
        break
    
    answer.append(N % B)
    N = N // B

for i in answer[::-1]:
    print(i, end='')