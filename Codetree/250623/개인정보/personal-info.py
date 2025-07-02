n = 5
name = []
height = []
weight = []

for _ in range(n):
    nm, he, we = input().split()
    name.append(nm)
    height.append(int(he))
    weight.append(float(we))

# Please write your code here.
class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    
    def __str__(self):
        return f'{self.name} {self.height} {self.weight}'

students = [Student(name[i], height[i], weight[i]) for i in range(n)]
students.sort(key= lambda x: x.name)
print('name')
for i in range(n):
    print(students[i].__str__())
print()
print('height')
students.sort(key= lambda x: -x.height)
for i in range(n):
    print(students[i].__str__())