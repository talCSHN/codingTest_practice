n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
whiteCount = 0 
blackCount = 0
curr_color = None
class ColorCounter:
    def __init__(self, whiteCount, blackCount, curr_color):
        self.whiteCount = whiteCount
        self.blackCount = blackCount
        self.curr_color = curr_color
    
    def getColor(self):
        return self.curr_color

init_arr = [ColorCounter(whiteCount, blackCount, curr_color) for _ in range(100010)]
curr_pos = 50005

for i in range(n):
    if (dir[i] == 'R'):
        for j in range(curr_pos, curr_pos + x[i]):
            if (init_arr[j].whiteCount >= 2 and init_arr[j].blackCount >= 1):
                init_arr[j].blackCount += 1
                init_arr[j].curr_color = 'g'
            else:
                init_arr[j].blackCount += 1
                init_arr[j].curr_color = 'b'
        curr_pos = curr_pos + x[i] - 1
    elif (dir[i] == 'L'):
        for k in range(curr_pos - x[i] + 1, curr_pos + 1):
            if (init_arr[k].whiteCount >= 1 and init_arr[k].blackCount >= 2):
                init_arr[k].whiteCount += 1
                init_arr[k].curr_color = 'g'
            else:
                init_arr[k].whiteCount += 1
                init_arr[k].curr_color = 'w'
        curr_pos = curr_pos - x[i] + 1

total_white = 0
total_black = 0
total_gray = 0
for i in range(len(init_arr)):
    if(init_arr[i].getColor() == 'w'):
        total_white += 1
    elif(init_arr[i].getColor() == 'b'):
        total_black += 1
    elif(init_arr[i].getColor() == 'g'):
        total_gray += 1

print(f'{total_white} {total_black} {total_gray}')