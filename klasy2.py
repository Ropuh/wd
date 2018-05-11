class Student:
    imie = ""
    wiek = ""
    nazwisko = ""
    def __init__(self):
        print('Student:')
        self.imie=input('Podaj imie?')
        self.wiek=int(input('Podaj wiek?'))
        self.nazwisko=input('Podaj nazwisko?')
    def Podsumowanie(self):
        print ('Student ma na imie ' + self.imie + ' i ma ' + str(self.wiek) + ' lat')

osoba1 = Student()
osoba2 = Student()
osoba3 = Student()

osoba1.Podsumowanie()
osoba2.Podsumowanie()
osoba3.Podsumowanie()

print(osoba1.nazwisko)
