class Telewizor:
    liczbaKanalow=8
    kanaly=['TVP1','TVP2','TVP3','TVN', 'Polsat','TVN24', 'Polsat News', 'TVP Info']
    nrKanalu = 0
    def powitanie(self):
        print("Hello!!!")
    def wyswietlKanal(self):
        print(self.liczbaKanalow)
    def __init__(self):
        print("TV is on")
        print("Ustawiony kanal: ")
        self.kanaly[self.nrKanalu]
    def listaKanalow(self):
        for i in self.kanaly:
            print (i)
    def ustawKanal(self,wpisanyKanal):
        self.nrKanalu=wpisanyKanal
        
    def ustawionyKanal(self):
        print("Ustawiony kanal: ", self.kanaly [self.nrKanalu])
        

mojTV=Telewizor()
mojTV.powitanie()
mojTV.wyswietlKanal()
mojTV.listaKanalow()
print('--')
mojTV.ustawKanal(int(input('Jaki kanal wysietlic?')))
print('--')
mojTV.ustawionyKanal()

