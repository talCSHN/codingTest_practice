a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def calculate(a, o, c):
    if (o == '+'):
        print(f'{a} + {c} = {a + c}')
    elif (o == '-'):
        print(f'{a} - {c} = {a - c}')
    elif (o == '*'):
        print(f'{a} * {c} = {a * c}')
    elif (o == '/'):
        print(f'{a} / {c} = {int(a / c)}')
    else:
        print(False)

calculate(a, o, c)