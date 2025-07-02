secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class Spy:
    def __init__(self, s, p, t):
        self.secret = s
        self.place = p
        self.time = t

spy = Spy(secret_code, meeting_point, time)
print(f'secret code : {spy.secret}')
print(f'meeting point : {spy.place}')
print(f'time : {spy.time}')
