# Zadanie 1
#
# Создать класс с двумя переменными. Добавить функцию вывода на экран и функцию изменения
# этих переменных. Добавить функцию, которая находит сумму значений этих переменных, и функцию которая
#  находит наибольшее значение из этих двух переменных.

class MyClass:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def display(self):
        print(f"Переменная 1: {self.var1}")
        print(f"Переменная 2: {self.var2}")

    def change(self, new_var1, new_var2):
        self.var1 = new_var1
        self.var2 = new_var2
        print("Значения переменных успешно изменены!")

    def sum_values(self):
        return self.var1 + self.var2

    def find_max(self):
        return max(self.var1, self.var2)

# Пример использования класса
obj = MyClass(10, 5)
print("Исходные значения переменных:")
obj.display()

new_var1 = 20
new_var2 = 15
obj.change(new_var1, new_var2)

print("Новые значения переменных:")
obj.display()

print(f"Сумма значений переменных: {obj.sum_values()}")
print(f"Наибольшее значение: {obj.find_max()}")

# Zadanie 2
#
# Описать класс, реализующий десятичный счетчик, который может увеличивать или уменьшать свое значение
#  на единицу в заданном диапазоне. Предусмотреть инициализацию счетчика значениями по умолчанию и
# произвольными значениями. Счетчик имеет два метода: увеличения и уменьшения, — и свойство, позволяющее
#  получить его текущее состояние. Написать программу, демонстрирующую все возможности класса.

class DecimalCounter:
    def __init__(self, min_value=0, max_value=100, initial_value=0):
        self.min_value = min_value
        self.max_value = max_value
        self.value = initial_value

    def increment(self):
        if self.value < self.max_value:
            self.value += 1
        else:
            print("Достигнуто максимальное значение.")

    def decrement(self):
        if self.value > self.min_value:
            self.value -= 1
        else:
            print("Достигнуто минимальное значение.")

    @property
    def current_value(self):
        return self.value

counter1 = DecimalCounter()  # Инициализация счетчика со значениями по умолчанию
print("Текущее значение счетчика (по умолчанию):", counter1.current_value)

counter1.increment()
counter1.increment()
print("Новое значение счетчика после двух инкрементов:", counter1.current_value)

counter1.decrement()
print("Новое значение счетчика после декремента:", counter1.current_value)

counter2 = DecimalCounter(-10, 10, 5)  # Инициализация счетчика с произвольными значениями
print("Текущее значение счетчика (произвольные значения):", counter2.current_value)

counter2.decrement()
print("Новое значение счетчика после декремента:", counter2.current_value)

# Zadanie 3
#
# Реализуйте класс Shop. Предусмотреть возможность работы с произвольным числом продуктов, поиска
#  продуктов по названию, добавления их в магазин и удаления продуктов из него.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return

    def find_product_by_name(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product
        return None

if __name__ == '__main__':
    shop = Shop()

    product1 = Product("Молоко", 50)
    product2 = Product("Хлеб", 30)

    shop.add_product(product1)
    shop.add_product(product2)

    found_product = shop.find_product_by_name("Хлеб")
    if found_product:
        print(f"Найден продукт: {found_product.name}, Цена: {found_product.price}")
    else:
        print("Продукт не найден")

    shop.remove_product("Молоко")

    found_product = shop.find_product_by_name("Молоко")
    if found_product:
        print("Найден продукт:", found_product.name)
    else:
        print("Продукт не найден")

# Zadanie 4
#
# Реализуйте класс MoneyBox, для работы с виртуальной копилкой. Каждая копилка имеет ограниченную
# вместимость, которая выражается целым числом – количеством монет(capacity -вместимость), которые можно
# положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке, предоставлять
# возможность добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет,
# не превышая ее вместимость.
# Класс должен иметь следующий вид:
# class MoneyBox:
#     def__init__(self, capacity) :
#     #конструктор с аргументом- вместимость копилки
#     def can_add(self,v)
#     #True, если можно добавить v монет, False иначе
#     def add(self,v)
#     #положить v монет в копилку
#
# При создании копилки, число монет в ней равно 0.
# Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True.


class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.coins = 0

    def can_add(self, v):
        return self.coins + v <= self.capacity

    def add(self, v):
        if self.can_add(v):
            self.coins += v
            print(f"Добавлено {v} монет. В копилке теперь {self.coins} монет.")
        else:
            print(f"Нельзя добавить {v} монет. Вместимость копилки превышена.")

if __name__ == '__main__':
    money_box = MoneyBox(10)
    print(f"Вместимость копилки: {money_box.capacity}")

    money_box.add(5)
    money_box.add(3)
    money_box.add(4)


