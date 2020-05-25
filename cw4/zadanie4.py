class NaZakupy:
    def __init__(self, nazwa, ilosc, jednostka, cena):
        self.nazwa = nazwa
        self.ilosc = ilosc
        self.jednostka = jednostka
        self.cena = cena

    def wyswietl(self):
        print('Nazwa:',self.nazwa, 'ilosc: ',self.ilosc, 'jednostka: ',
              self.jednostka, 'cena: ', self.cena)

    def ile_produktu(self):
        print(self.ilosc, self.jednostka)

    def ile_kosztuje(self):
        koszt = self.cena*self.ilosc
        print(str(koszt))

zakupy = NaZakupy('jaja',2,'sztuki',12)

zakupy.wyswietl()
zakupy.ile_produktu()
zakupy.ile_kosztuje()