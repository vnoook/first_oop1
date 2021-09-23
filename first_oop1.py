class MyFirstClass():
    x1 = 111
    def __init__(self):
        x1 = 444
        x2 = 222

print(f'{MyFirstClass.x1 = }')
# MyFirstClass.x1 = 333
# print(f'{MyFirstClass.x1 = }')

a = MyFirstClass()
print(f'{a.x1 = }')
# a.x1 = 223344
# print(f'{a.x1 = }')



