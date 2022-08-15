class MyFirstClass:
    ''' описание класса __doc__ '''

    # статический атрибут, свойство класса
    x1 = 000

    # конструктор
    def __init__(self):
        # динамические атрибуты, свойства экземпляра
        self.x1 = 111
        self.x2 = 222
        self.x3 = 333
        self._y1 = 'protect1'  #  защищённый атрибут
        self.__y2 = 'privat1'  #  приватный атрибут

    # метод получения имени
    def get_obj_name(self):
        for glob_name, glob_val in globals().items():
            if glob_val is self:
                return glob_name


if __name__ == '__main__':
    # эксперименты с классом
    print(MyFirstClass.__dict__)
    print(MyFirstClass().__dict__)
    print()
    print(MyFirstClass.get_obj_name(MyFirstClass))
    print()
    print(MyFirstClass.__mro__)
    print()
    print(id(MyFirstClass))
    print(id(MyFirstClass()))
    print()
    print(f'обращаюсь к статическому атрибуту "x1" класса "{MyFirstClass.__name__}"')
    print(f'{MyFirstClass.x1 = }')
    print('_'*150)

    # эксперименты с экземпляром
    a = MyFirstClass()
    print(f'создаю объект "{a.get_obj_name()}" и обращаюсь к его атрибуту "x1" двумя способами')
    print(f'{a.x1 = }  ...  {a.__getattribute__("x1") = }')
    print()

    print(f'меняю значение атрибута "x1" объекта "{a.get_obj_name()}" и обращаюсь к нему двумя способами')
    a.x1 = 123
    print(f'{a.x1 = }  ...  {a.__getattribute__("x1") = }')
    print()

    print(f'меняю в классе "{MyFirstClass.__name__}" атрибут и обращаюсь к нему')
    MyFirstClass.x1 = 333
    print(f'{MyFirstClass.x1 = } ... {MyFirstClass.__getattribute__(MyFirstClass, "x1") = }')
    print()

    print(f'обращаюсь к атрибуту объекта')
    print(f'{a.x1 = }  ...  {a.__getattribute__("x1") = }')
    print()

    for val in list(globals()):
        print(f'globals()[{val}] = {globals()[val]}   ...   {type(globals()[val]) = }')

    print()

    for glob_name, glob_val in list(globals().items()):
        if '__' not in glob_name:
            print(glob_name, glob_val)

    print()

    print(dir(MyFirstClass))
    print(dir(MyFirstClass()))
    print(dir(a))

    print()

    method_list = [method for method in dir(MyFirstClass) if method.startswith('_') is False]
    print(method_list)

    method_list = [method for method in dir(MyFirstClass()) if method.startswith('_') is False]
    print(method_list)

    print()
    print(a.__dict__)
    print(a.__dir__())
    print(dir(a))
