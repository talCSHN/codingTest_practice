text = input()
pattern = input()

# Please write your code here.
partialTxt = ""
def showIdx():
    global partialTxt
    for i in range(0, (len(text) - len(pattern) + 1), len(pattern)):
        for j in range(i, i + len(pattern)):
            partialTxt += text[j]
    if (pattern in partialTxt):
        print(i)
    else:
        print(-1)

showIdx()