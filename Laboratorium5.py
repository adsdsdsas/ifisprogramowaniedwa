# Napisz klasę Student oraz klasę dziedziczącą po niej GraduatedStudent. Nadaj im odpowiednie atrybuty.

class Student:
    def __init__(self, name, surname, grades):
        self.name = name
        self.surname = surname
        self.grades = grades


class GraduatedStudent(Student):
    def __init__(self, name, surname, grades, work):
        super().__init__(name, surname, grades)
        self.work = work

    @property                                                   # @property zamienia metodę w atrybut (zmienną) o wartości zwracanej (return) przez metodę
    def present_myself(self):                                   # czyli to tak, jakbyśmy stworzyli atrybut self.present_myself = f'Hi Im {self.name}..."
        return f'Hi Im {self.name} {self.surname} and I work at {self.work}'


kuba = GraduatedStudent('Arek', 'Arkowski', 4.45, 'McDonalds')
print(kuba.name)
print(kuba.present_myself)



# -------------------------------------------------------------------------------
# Stwórz klasę Car, a następnie utwórz trzy klasy SUV, Sport, MiniVan które będą dziedziczyć po klasie Car. Zdefiniuj odpowiednie atrybuty dla każdej z klas.

class Car:
    def __init__(self, model, wheels=4):
        self.model = model
        self.wheels = wheels

class SUV(Car):
    def __init__(self):
        self.drzwi = 4

    def open_drzwi(self):
        print('Otwarte!')

    def close_drzwi(self):
        print('Zamknięte :c')

class Sport(Car):
    def __init__(self):
        self.booster = 150

    def boost(self):
        print('Woah!!! Im so fast!')

class Tir(Car):
    def __init__(self):
        super().__init__(4)
        self.naczepa = 1

    def odczep_sie(self):
        self.naczepa = 0



# -------------------------------------------------------------------------------
# Napisz domieszkę AddableMixin, powinna ona udostępniać metodę pozwalającą na dodawanie dwóch obiektów do siebie.
class AddableMixin:
    def __add__(self, other):
        new_list = list(self.value)
        new_list.append(other)
        return new_list
    # raise NotImplementedError('Sorry I havent wrote this exercise yet')

# Napisz domieszkę FromJSONMixin, powinna ona udostępniać metodą pozwalającą na wczytywanie wartości atrybutów z pliku JSON.
import json

class FromJSONMixin:
    def from_json(self):
        with open(self.filename, 'r') as f:
            return json.load(f)
        # raise NotImplementedError('Sorry I havent wrote this exercise yet')

class TakeJsonListAndAddSomething(AddableMixin, FromJSONMixin):
    def __init__(self, filename):
        self.filename = filename
        self.value = self.from_json()


my_list_and_seven = TakeJsonListAndAddSomething('lab5.json')

print(my_list_and_seven + 7)



# -------------------------------------------------------------------------------
# zadania z metod statycznych i klasowych:

from datetime import datetime, timedelta

class Data:
    def __init__(self, rok, miesiac, dzien):
        self.rok = rok
        self.miesiac = miesiac
        self.dzien = dzien

    @classmethod
    def dzisiaj(cls):
        dzis = datetime.now()
        return cls(dzis.year, dzis.month, dzis.day)

    @classmethod        # Napisz metodę klasy dla klasy Data zwracającą nowy obiekt z datą wczorajszą.
    def wczoraj(cls):
        dzis = datetime.now()
        one_day = timedelta(days=1)                             # https://docs.python.org/3/library/datetime.html#datetime.timedelta
        wczoraj = dzis - one_day
        return cls(wczoraj.year, wczoraj.month, wczoraj.day)

    @staticmethod       # Napisz metodę statyczną dla klasy Data zmieniającą datę zapisaną w stringu w formacie USA "MM/DD/YYYY" na format europejski "DD/MM/YYYY".
    def change_format(datestring):
        return f'{datestring[3:5]}.{datestring[:2]}.{datestring[6:]}'


d = Data.dzisiaj()  # Utworzy nową instancję obiektu z klasy Data z dzisiejszą datą.
w = Data.wczoraj()

print(f'Wczorajsza data: {w.dzien}.{w.miesiac}.{w.rok}\nDzisiejsza data: {d.dzien}.{d.miesiac}.{d.rok}')
print(d.change_format(f'Dzisiejsza data ale po polsku: {d.dzien}.{d.miesiac}.{d.rok}'))



# -------------------------------------------------------------------------------

# W starożytnej Grecji żyli filozofowie tacy jak Sokrates, Platon, czy Arystoteles.
# Prowadzili oni ze sobą liczne dysputy na rozmaite tematy.
# Jednym z nich był Platon.
# Platon sądził, że istnieje świat idei, w którym znajdują się idealne byty (a właść. idee tych bytów), np. Idealny Królik
# oraz świat ludzi, niedoskonały, w którym znajdują się nieidealne odzwierciedlenia tych idei, np. królik Franek.
# W pythonie jest bardzo podobnie - idee to klasy, a byty to obiekty:

class Krolik:                                   # klasa Królik - idea królika
    def __init__(self, usz, ogo, lap, im):
        self.uszy = usz                         # każdy królik ma uszy,
        self.ogonek = ogo                       # łapki,
        self.lapki = lap                        # ogonek,
        self.imie = im                          # oraz imię

    def skakanie(self):                         # każdy królik potrafi również skakać
        print('hop')


krolikfranek = Krolik(2, 1, 4, 'Franek')        # obiekt krolikfranek - nieidealny byt odzwierciedlający ideę (klasę) Królika

print(krolikfranek.imie)                        # królik Franek ma 2 uszy, 1 ogonek, 4 łapki i jedno imię
krolikfranek.skakanie()

krolikalbert = Krolik(1, 1, 4, 'Albert')        # obiekt krolikalbert - inny nieidealny byt odzwierciedlający ideę Królika

print(krolikalbert.imie)                        # królik Albert stracił ucho podczas wojny na Bałkanach - zostało mu tylko jedno :c
krolikalbert.skakanie()                         # jednak wciąż potrafi skakać!
