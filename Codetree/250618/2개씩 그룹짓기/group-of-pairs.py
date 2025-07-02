n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
sumList = []
nums.sort()
for i in range(len(nums) // 2):
    sumList.append(nums[i] + nums[len(nums) - 1 - i])
print(max(sumList))
