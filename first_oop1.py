
class MyFirstClass():
    x1 = 111
    # print('__common__')
    # print(f'{x1 = }')
    # print()
    def __init__(self):
        x1 = 444
        x2 = 222
        # print('__init__')
        # print(x2)
        # print(self.x2)
        # print(MyFirstClass.x2)
        # print()

print(f'{MyFirstClass.x1 = }')

MyFirstClass.x1 = 333
print(f'{MyFirstClass.x1 = }')

a = MyFirstClass()

print(f'{a.x1 = }')

a.x1 = 223344
print(f'{a.x1 = }')

print(f'{MyFirstClass.x1 = }')

