class MyFirstClass():
    x1 = 111
    def __init__(self):
        x1 = 444
        x2 = 222

print()
print(f'{MyFirstClass.x1 = }')

a = MyFirstClass()
print(f'{a.x1 = }')
print(f'{a.__getattribute__("x1") = }')
a.x1 = 123
print(f'{a.x1 = }')
print()

MyFirstClass.x1 = 333
print(f'{MyFirstClass.x1 = }')
print()

print(f'{a.x1 = }')
print(f'{a.__getattribute__("x1") = }')
print()

# print(f'{a.x1 = }')
# a.x1 = 223344
# print(f'{a.x1 = }')

for val in list(globals()):
    print(f'globals()[{val}] = {type(globals()[val])}, {globals()[val]}')

