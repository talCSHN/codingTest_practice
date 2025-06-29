m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
day_of_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
elapsed_days = 0
is_last = False
if (m1 > m2 or (m1 == m2 and d1 > d2)):
    is_last = True

while True:
    if (m1 > m2 or (m1 == m2 and d1 > d2)):
        if (m1 == m2 and d1 == d2):
            # is_last = True
            break
        d2 += 1
        elapsed_days += 1
        if (d2 > day_of_months[m2]):
            m2 += 1
            d2 = 1
    else:
        if (m1 == m2 and d1 == d2):
            # is_last = False
            break

        d1 += 1
        elapsed_days += 1

        if (d1 > day_of_months[m1]):
            m1 += 1
            d1 = 1

default_idx = 1 # Mon
# print(is_last)
day_cal = elapsed_days % 7
# print(day_cal)
if (is_last == False):
    if (default_idx + day_cal > 6):
        print(days[0])
    else:
        print(days[default_idx + day_cal])
else:
    if (default_idx - day_cal >= 0):
        print(days[default_idx - day_cal])
    else:
        print(days[default_idx - day_cal + 7])
