n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.
'''
4
2036-12-27 Sun Snow
2052-08-28 Wed Rain
2043-03-21 Sat Sun
2077-08-19 Thu Rain
date = [2036-12-27, 2052-08-28, 2043-03-21, 2077-08-19]
day = [Sun, Wed, Sat, Thu]
weather = [Snow, Rain, Sun, Rain]
'''
class WeatherDays:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

    def __str__(self):
        return f'{self.date} {self.day} {self.weather}'

rainyDays = []
for i in range(n):
    if (weather[i] == 'Rain'):
        rainyDays.append(WeatherDays(date[i], day[i], weather[i]))

rainyDays.sort(key= lambda x : x.date)
print(rainyDays[0].__str__())
