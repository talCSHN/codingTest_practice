# # 카톡 친구 자동 삽입
# kakaoFriends = [('호날두', 777), ('메시', 200), ('음바페', 100), ('홀란드', 50), ('노무현', 1)]
# # len(kakaoFriends)
# # print(kakaoFriends[1])
# # tp = kakaoFriends[1]
# # print(tp[1])

# def insertFriend(friend, katokCount):
#     posit = -1
#     kakaoFriends.append(None)
#     kLen = len(kakaoFriends)

#     for i in range(kLen - 1):
#         friendTuple = kakaoFriends[i]
#         if katokCount >= friendTuple[1]:
#             posit = i
#             break
#     if posit == -1:
#         posit = len(kakaoFriends)
#         kakaoFriends[posit - 1] = (friend, katokCount)
#         return

#     if posit < 0 or posit > kLen:
#         print('out of range')
#         return
#     for j in range(kLen - 1, posit, -1):
#         kakaoFriends[j] = kakaoFriends[j - 1]
#         kakaoFriends[j - 1] = None
#     kakaoFriends[posit] = (friend, katokCount)

# if __name__ == '__main__':

#     while True:
#         data = input('추가할 친구 : ')
#         count = int(input('카톡 횟수'))
#         if count < 0:
#             print('카톡 횟수는 양수여야 함')
#             continue
#         insertFriend(data, count)
#         print(kakaoFriends)

#         controller = int(input('1 : 프로그램 종료 >>>>>> '))
#         if controller == 1:
#             break
#         else:
#             print('잘못된 번호 입력')
#             continue