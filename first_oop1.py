class MyFirstClass():
    x1 = 111
    print('__common__')
    print(f'{x1 = }')
    print()
    def __init__(self):
        x2 = 222
        x1 = 444
        print('__init__')
        print(x2)
        print(self.x2)
        print(MyFirstClass.x2)
        print()

print(f'{MyFirstClass.x1 = }')

MyFirstClass.x1 = 333

print(f'{MyFirstClass.x1 = }')
