n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
class ColorStat:
    def __init__(self, currColor):
        self.currColor = currColor
    
    def getCurrColor(self):
        return self.currColor

init_arr = [ColorStat('g') for i in range(200010)]
curr_pos = 100005
for i in range(n):
    if(dir[i] == 'R'):
        for j in range(curr_pos, curr_pos + x[i]):
            init_arr[j].currColor = 'b'
        curr_pos = curr_pos + x[i] - 1
    elif(dir[i] == 'L'):
        for k in range(curr_pos - x[i] + 1, curr_pos + 1):
            init_arr[k].currColor = 'w'
        curr_pos = curr_pos - x[i] + 1

whiteCount = 0
blackCount = 0
for i in range(len(init_arr)):
    if(init_arr[i].getCurrColor() == 'w'):
        whiteCount += 1
    elif(init_arr[i].getCurrColor() == 'b'):
        blackCount += 1

print(f'{whiteCount} {blackCount}')