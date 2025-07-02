n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Please write your code here.
class Student:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math

    def __str__(self):
        return f'{self.name} {self.korean} {self.english} {self.math}'

students = [Student(name[i], korean[i], english[i], math[i]) for i in range(n)]
students.sort(key= lambda x: (-x.korean, -x.english, -x.math))

for i in range(n):
    print(students[i].__str__())