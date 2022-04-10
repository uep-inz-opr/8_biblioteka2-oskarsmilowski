from dataclasses import dataclass, astuple
from operator import itemgetter
import ast

@dataclass(frozen=True, order=True)
class Ksiazka:
    tytul: str
    autor: str
    rok: int

@dataclass(frozen=True, order=True)
class Biblioteka:
    ksiazki: dict() # slownik gdzie kluczem jest krotka tytul,autor,rok a wartością liczba egzemplarzy ksiązek 
    czytelnicy: dict() # zagniezdzony slownik, kazdy czytelnik ma swoj slownik wypozyczen {tytul: 1}


    def pobierz_czytelnika(self,imie) -> bool:
        if imie in self.czytelnicy:
            return True
        else:
            return False
    
    def sprawdz_stan(self,tytul_ksiazki) -> bool:
        for ksiazka, egzemplarze in self.ksiazki.items():
            if ksiazka.tytul == tytul_ksiazki:
                return egzemplarze > 0

    def ksiazka_po_tytule(self,tytul_ksiazki) -> Ksiazka:
        for ksiazka in self.ksiazki:
            if ksiazka.tytul == tytul_ksiazki:
                return ksiazka
    
    def sprawdz_czy_ta_sama(self,czytelnik, tytul) -> bool:
        if czytelnik in self.czytelnicy:
            if tytul in self.czytelnicy[czytelnik]:
                return True
        return False
    
    def sprawdz_czy_trzy(self,czytelnik) -> bool:
        if czytelnik in self.czytelnicy:
            return len(self.czytelnicy[czytelnik]) == 3
            


    def dodaj_ksiazke(self,ksiazka):
        if ksiazka not in self.ksiazki:
            self.ksiazki[ksiazka] = 1
        else:
            self.ksiazki[ksiazka] += 1
        return "True"
    
    def wypozycz_ksiazke(self,czytelnik, tytul):
        if not self.pobierz_czytelnika(czytelnik) and self.sprawdz_stan(tytul):
            self.czytelnicy[czytelnik] = {tytul: 1}
            ksiazka = self.ksiazka_po_tytule(tytul)
            self.ksiazki[ksiazka] -= 1
            return "True"
        else:
            return "False"
        if self.sprawdz_stan(tytul) and not self.sprawdz_czy_ta_sama(czytelnik, tytul) and not self.sprawdz_czy_trzy(czytelnik):
            self.czytelnicy[czytelnik][tytul] = 1
            ksiazka = self.ksiazka_po_tytule(tytul)
            self.ksiazki[ksiazka] -= 1
            return "True"
        else:
            return "False"

    def oddaj_ksiazke(self,czytelnik, tytul):
        if tytul not in self.czytelnicy[czytelnik]:
            return "False"
        else:
            ksiazka = self.ksiazka_po_tytule(tytul)
            self.ksiazki[ksiazka] += 1
            del self.czytelnicy[czytelnik][tytul]
            return "True"




def main():
    liczba_akcji = input()
    biblioteka = Biblioteka({},{})

    for _ in range(int(liczba_akcji)):
        dane_wejsciowe = eval(input())
        if dane_wejsciowe[0] == "dodaj":
            ksiazka = Ksiazka(dane_wejsciowe[1], dane_wejsciowe[2], int(dane_wejsciowe[3]))
            wynik = biblioteka.dodaj_ksiazke(ksiazka)
        elif dane_wejsciowe[0] == "wypozycz":
            wynik = biblioteka.wypozycz_ksiazke(dane_wejsciowe[1], dane_wejsciowe[2])
        else:
            wynik = biblioteka.oddaj_ksiazke(dane_wejsciowe[1], dane_wejsciowe[2])
        print(wynik)

        

if __name__ == "__main__":
    main()
