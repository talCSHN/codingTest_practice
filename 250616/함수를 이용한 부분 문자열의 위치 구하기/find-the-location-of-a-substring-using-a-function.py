text = input()
pattern = input()

# Please write your code here.
def showIdx():
    for i in range(0, len(text) - len(pattern) + 1):
        if (text[i:i+len(pattern)] == pattern):
            print(i)
            return
    print(-1)

showIdx()