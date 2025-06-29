m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
days_of_months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_of_week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
elapsed_days = 1
while True:
    if (m1 == m2 and d1 == d2):
        break

    d1 += 1
    elapsed_days += 1

    if (d1 > days_of_months[m1]):
        m1 += 1
        d1 = 1

day_count = elapsed_days // 7
day_count_else = (elapsed_days % 7)

if (day_count_else >= days_of_week.index(A) and A != 'Sun'):
    day_count += 1
    print(day_count)
else:
    print(day_count)