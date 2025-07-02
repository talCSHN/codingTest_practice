product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
class Item:
    def __init__(self, name = 'codetree', code = 50):
        self.name = name
        self.code = code
    def __str__(self):
        return f'product {self.code} is {self.name}'

item1 = Item()
item2 = Item(product_name, product_code)

print(item1.__str__())
print(item2.__str__())