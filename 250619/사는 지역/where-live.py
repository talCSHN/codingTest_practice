n = int(input())
name = []
street_address = []
region = []

# for _ in range(n):
#     n_i, s_i, r_i = input().split()
#     name.append(n_i)
#     street_address.append(s_i)
#     region.append(r_i)

# Please write your code here.
people = []
class People:
    def __init__(self, name='', address='', region=''):
        self.name = name
        self.address = address
        self.region = region
    def __str__(self):
        return f'name {self.name}\naddr {self.address}\ncity {self.region}'

for _ in range(n):
    pname, address, pregion = tuple(input().split())
    people.append(People(pname, address, pregion))

people.sort(key= lambda x : x.name)
print(people[-1].__str__())


