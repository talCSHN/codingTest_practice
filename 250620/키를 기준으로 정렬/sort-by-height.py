n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.
class Students:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    def __str__(self):
        return f'{self.name} {self.height} {self.weight}'

studentList = [Students(name[i], height[i], weight[i]) for i in range(n)]
studentList.sort(key=lambda x: x.height)

for i in range(n):
    print(studentList[i].__str__())