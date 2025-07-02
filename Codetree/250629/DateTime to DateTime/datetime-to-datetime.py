a, b, c = map(int, input().split())

# Please write your code here.
# elapsed_min = 0
# curr_day = 11
# curr_time = 11
# curr_min = 11

dif_day = a - 11
dif_hour = b - 11
dif_min = c - 11

day_to_min = dif_day * 24 * 60
hour_to_min = dif_hour * 60
result = day_to_min + hour_to_min + dif_min

if (result < 0):
    print(-1)
else:
    print(result)


# while True:
#     if (curr_day == a and curr_time == b and curr_min == c):
#         break

#     elapsed_min += 1
#     curr_min += 1
    
#     if (curr_min > 59):
#         curr_time += 1
#         curr_min = 0
    
#     if (curr_time >= 24):
#         curr_day += 1
#         curr_time = 0

# print(elapsed_min)