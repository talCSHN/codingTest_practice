n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
A = arr
for i in range(m):
    result = 0
    result += sum(A[queries[i][0] - 1 : queries[i][1]])
    
    print(result)
        