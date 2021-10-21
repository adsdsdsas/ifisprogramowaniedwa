import random

'''ZADANIE 1'''
class Pudelko:
    def __init__(self, width, length, height):
        self.size = (width, length, height)
        self.cap = width + length + height


    def change_size(self, new_size):
        self.size = new_size
        self.cap = self.size[0] + self.size[1] + self.size[2]

    @property
    def capacity(self):
        if self.cap == 3:
            return 1
        elif 3 < self.cap < 6:
            return 2
        elif self.cap == 6:
            return 3
        elif self.cap > 6:
            return 4


pudelko1 = Pudelko(1, 1, 1)
print(f'capacity of pudelko1: {pudelko1.capacity}')


'''ZADANIE 2'''

class Kosmita:
    def __init__(self, name, age, planet):
        self.name = name
        self.age = age
        self.planet = planet


kosmita_roman = Kosmita("Roman", 54, "Earth")
print(f'Cześć, jestem {kosmita_roman.name} z planety {kosmita_roman.planet}')


'''ZADANIE 3'''

class Rakieta:
    def __init__(self, mass, fuel):
        self.mass = mass
        self.fuel = fuel

    def fuel_usage(self, h):
        usage = self.mass * h
        if usage <= self.fuel:
            print("3, 2, 1, START!")
        else:
            print("O nie! Mamy za mało paliwa!")


rakieta1 = Rakieta(10, 5000)

rakieta1.fuel_usage(500)


'''ZADANIE 4'''

class CrazyStrings:
    def __init__(self, text):
        self.text = text


    @property
    def leet(self):
        string = self.text
        new_string1 = string.replace("a", "4")
        new_string2 = new_string1.replace("h", "5")
        new_string3 = new_string2.replace("b", "8")
        new_string4 = new_string3.replace("o", "0")
        new_string5 = new_string4.replace("l", "1")
        return new_string5


    @property
    def poke(self):
        counter = 0
        new_text = ""
        for x in self.text:
            if counter %2 == 0:
                new_text += x.upper()
                counter += 1
            else:
                new_text += x.lower()
                counter += 1
        return new_text


    def rand(self):
        a = random.randint(1, 100)
        if a %2 == 0:
            return self.poke
        else:
            return self.leet


crazy_string1 = CrazyStrings("Hejka naklejka co tam u cb zastanawiam sie kiedy sie zobaczymy uwu")
print(crazy_string1.rand())
print(crazy_string1.rand())
print(crazy_string1.rand())
print(crazy_string1.rand())
print(crazy_string1.rand())