class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


class Cricketer(Person):
    def __init__(self, name, age, height, weight):
        super().__init__(name, age, height, weight)

    def __lt__(self, other):
        return self.age < other.age


Sakib = Cricketer('Sakib', 38, 68, 91)
Mushfiq = Cricketer('Mushfiq', 36, 55, 82)
Mustafiz = Cricketer('Mustafiz', 27, 69, 86)
Riyad = Cricketer('Riyad', 39, 72, 92)

youngest_player = min([Sakib, Mushfiq, Mustafiz, Riyad])
print("Youngest player:", youngest_player.name)

