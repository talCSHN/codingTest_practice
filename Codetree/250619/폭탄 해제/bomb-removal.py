unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
class Bomb:
    def __init__(self, code, color, time):
        self.code = code
        self.color = color
        self.time = time
    
    def __str__(self):
        return f'code : {self.code}\ncolor : {self.color}\nsecond : {self.time}'

bomb = Bomb(unlock_code, wire_color, seconds)
print(bomb.__str__())