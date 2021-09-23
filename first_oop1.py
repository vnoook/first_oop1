class MyFirstClass:
    # статический атрибут
    x1 = 000

    def __init__(self):
        # динамические атрибуты
        self.x1 = 111
        self.x2 = 222
        self.x3 = 333

    def get_obj_name(self):
        for glob_name, glob_val in globals().items():
            if glob_val is self:
                return glob_name


print()
print(f'обращаюсь к статическому атрибуту x1 класса {MyFirstClass.__name__}')
print(f'{MyFirstClass.x1 = }')
print()

a = MyFirstClass()
print(f'создаю объект {a.get_obj_name()} и обращаюсь к его атрибуту двумя способами')
print(f'{a.x1 = }  ...  {a.__getattribute__("x1") = }')
print()

print(f'меняю значение атрибута объекта {a.get_obj_name()} и обращаюсь к нему')
a.x1 = 123
print(dir(a.x1))

print(f'{a.x1 = }  ...  {a.__getattribute__("x1") = }')
print()

print(f'меняю в классе {MyFirstClass.__name__} атрибут и обращаюсь к нему')
MyFirstClass.x1 = 333
print(f'{MyFirstClass.x1 = }')
print()

# обращаюсь к атрибуту объекта
print(f'{a.x1 = }  ...  {a.__getattribute__("x1") = }')
print()

# print(f'{a.x1 = }')
# a.x1 = 223344
# print(f'{a.x1 = }')

# for val in list(globals()):
#     print(f' globals()[{val}] = {type(globals()[val])}, {globals()[val]}')
