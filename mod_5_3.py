"""
Домашняя работа по уроку "Перегрузка операторов"

Ваша задача:
Цель: применить знания о перегрузке арифметических операторов и операторов сравнения.

Задача "Нужно больше этажей":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Специальные методы класса".
"""
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor): #  Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку "Такого этажа не существует".
        if 1 < new_floor < self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
            else:
                print('Такого этажа не существует')


    def __len__(self):  # возврат кол-ва этажей здания
        return self.number_of_floors

    def __str__(self):    # возврат строки: "Название: <название>, кол-во этажей: <этажи>"
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}.'

    def __eq__(self, other):    # Методом сравнения на равенства: возвращаем True, если количество этажей self == other
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            return False

    def __lt__(self, other): # Метод сравнения "меньше чем"
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            return NotImplemented

    def __le__(self, other):    # Метод сравнения "меньше или равно"
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            return NotImplemented

    def __gt__(self, other):    # Метод сравнения "больше чем"
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            return NotImplemented

    def __ge__(self, other): # Метод сравнения "больше или равно"
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            return NotImplemented

    def __ne__(self, other):    # Метод сравнения на неравенство
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            return True

    def __add__(self, value):    # Метод добавления элемента в множество
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        elif isinstance(value, House):
            return House(self.name, self.number_of_floors + value.number_of_floors)
        else:
            return NotImplemented

    def __radd__(self, value):    # Метод симметричного сложения
        return self.__add__(value)

    def __iadd__(self, value):    # Метод сложения с присваиванием +=
        return self.__add__(value)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__

"""
Необходимо дополнить класс House следующими специальными методами:
__eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.

Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать 
результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.

__add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.

__radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).

Остальные методы арифметических операторов, где self - x, other - y:

Следует заметить, что other может быть не только числом, но и вообще любым объектом другого класса.
Для более точной логики работы методов __eq__, __add__  и других методов сравнения и арифметики перед выполняемыми 
действиями лучше убедиться в принадлежности к типу при помощи функции isinstance:
isinstance(other, int) - other указывает на объект типа int.
isinstance(other, House) - other указывает на объект типа House.

Пример результата выполнения программы:
Пример выполняемого кода:
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(h1 == h2) # __eq__
h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

Вывод на консоль:
Название: ЖК Эльбрус, кол-во этажей: 10
Название: ЖК Акация, кол-во этажей: 20
False
Название: ЖК Эльбрус, кол-во этажей: 20
True
Название: ЖК Эльбрус, кол-во этажей: 30
Название: ЖК Акация, кол-во этажей: 30
False
True
False
True
False

Примечания:
Методы __iadd__ и __radd__ не обязательно описывать заново, достаточно вернуть значение вызова __add__.
Более подробно о работе всех перечисленных методов можно прочитать здесь и здесь.

Успехов!"""