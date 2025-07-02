n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
answer = []
def divideEven(ary):
    for i in ary:
        if (i % 2 == 0):
            i = int(i / 2)
            answer.append(i)
        else:
            answer.append(i)
    print(*answer)

divideEven(arr)
