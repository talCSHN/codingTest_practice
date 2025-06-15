n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def makeAbsolute(ary):
    for i in range(len(ary)):
        if (ary[i] < 0):
            ary[i] = ary[i] * -1
    print(*ary)

makeAbsolute(arr)
