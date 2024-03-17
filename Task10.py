#exercise 1
class ChessPiece:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def attack(self, x, y):
        pass

class Queen(ChessPiece):
    def attack(self, x, y):
        if self.x == x or self.y == y or abs(self.x - x) == abs(self.y - y):
            print("Ферзь может атаковать эту клетку!")
        else:
            print("Ферзь не может атаковать эту клетку.")

class Pawn(ChessPiece):
    def attack(self, x, y):
        if abs(self.x - x) == 1 and self.y - y == 1:
            print("Пешка может атаковать эту клетку!")
        else:
            print("Пешка не может атаковать эту клетку.")

class Knight(ChessPiece):
    def attack(self, x, y):
        if (abs(self.x - x) == 1 and abs(self.y - y) == 2) or (abs(self.x - x) == 2 and abs(self.y - y) == 1):
            print("Конь может атаковать эту клетку!")
        else:
            print("Конь не может атаковать эту клетку.")

queen = Queen(1, 1, 'white')
pawn = Pawn(2, 2, 'black')
knight = Knight(3, 3, 'white')

queen.attack(3, 3)
pawn.attack(3, 4)
knight.attack(5, 5)
#exercise 2
class Carrier:
    def __init__(self, distance):
        self.distance = distance

    def transport_time(self):
        pass

    def transport_cost(self):
        pass

class Plane(Carrier):
    def transport_time(self):
        return self.distance // 500

    def transport_cost(self):
        return self.distance * 2

class Train(Carrier):
    def transport_time(self):
        return self.distance // 100

    def transport_cost(self):
        return self.distance * 1.5

class Car(Carrier):
    def transport_time(self):
        return self.distance // 60

    def transport_cost(self):
        return self.distance * 3

distance = 1000

plane = Plane(distance)
train = Train(distance)
car = Car(distance)

print(f"Для расстояния {distance} км:")
print(f"Время перевозки на самолете: {plane.transport_time()} часов")
print(f"Стоимость перевозки на самолете: {plane.transport_cost()} у.е.")
print(f"Время перевозки поездом: {train.transport_time()} часов")
print(f"Стоимость перевозки поездом: {train.transport_cost()} у.е.")
print(f"Время перевозки автомобилем: {car.transport_time()} часов")
print(f"Стоимость перевозки автомобилем: {car.transport_cost()} у.е.")
#exercise 3
class Живое:
    def __init__(self, возраст, еда):
        self.возраст = возраст
        self.еда = еда

    def есть(self):
        pass

    def проверить_состояние(self):
        pass

class Лиса(Живое):
    def есть(self, кролик):
        if isinstance(кролик, Кролик):
            кролик.умереть()
            self.еда = True

    def проверить_состояние(self):
        if self.возраст >= 5 or not self.еда:
            return False
        return True

class Кролик(Живое):
    def есть(self, растение):
        if isinstance(растение, Растение):
            растение.умереть()
            self.еда = True

    def проверить_состояние(self):
        if self.возраст >= 3 or not self.еда:
            return False
        return True

class Растение(Живое):
    def есть(self):
        self.еда = True

    def проверить_состояние(self):
        if self.возраст >= 2 or not self.еда:
            return False
        return True

лиса = Лиса(3, True)
кролик = Кролик(2, True)
растение = Растение(1, True)

print("Изначальное состояние:")
print("Лиса: живая" if лиса.проверить_состояние() else "Лиса: мертвая")
print("Кролик: живой" if кролик.проверить_состояние() else "Кролик: мертвый")
print("Растение: живое" if растение.проверить_состояние() else "Растение: мертвое")

лиса.есть(кролик)
кролик.есть(растение)
растение.есть()

print("\nПосле еды:")
print("Лиса: живая" if лиса.проверить_состояние() else "Лиса: мертвая")
print("Кролик: живой" if кролик.проверить_состояние() else "Кролик: мертвый")
print("Растение: живое" if растение.проверить_состояние() else "Растение: мертвое")