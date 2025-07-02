n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
## 유클리드 호제법 써야함 - 두 수 a, b의 최대공약수는 a를 b로 나눈 나머지와 b의 최대공약수와 같음
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcdList(n):
    if (len(n) == 1):
        return n[0]
    else:
        first = n[0]
        second = n[1]
        rest = n[2:]
        return gcdList([gcd(first, second)] + rest)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def lcmList(n):
    if (len(n) == 1):
        return n[0]
    else:
        first = n[0]
        second = n[1]
        rest = n[2:]
        return lcmList([lcm(first, second)] + rest)

print(lcmList(arr))
