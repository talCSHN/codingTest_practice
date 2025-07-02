user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class Character:
    def __init__(self, uid = "codetree", level = 10):
        self.uid = uid
        self.level = level
    
    def __str__(self):
        return f'user {self.uid} lv {self.level}'

character = Character()
character1 = Character(user2_id, user2_level)

print(character.__str__())
print(character1.__str__())

