n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
for i in nums:
    print(i, end= " ")
print()
nums.sort(reverse=True)
for j in nums:
    print(j, end=" ")

