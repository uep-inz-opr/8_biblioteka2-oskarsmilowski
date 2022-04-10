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


    def pobierz_czytelnika(imie) -> dict:
        if imie in self.czytelnicy:
            return self.czytelnicy[imie]
        else:
            return False
    
    def sprawdz_stan(tytul_ksiazki) -> bool:
        for (tytul,autor,rok), egzemplarze in self.ksiazki.items():
            if tytul == tytul_ksiazki:
                return egzemplarze > 0
    
    def sprawdz_czy_ta_sama(czytelnik, tytul) -> bool:
        if czytelnik in self.czytelnicy:
            if tytul in self.czytelnicy[czytelnik]:
                return true
        return false
    
    def sprawdz_czy_trzy(czytelnik) -> bool:
        if czytelnik in self.czytelnicy:
            return len(self.czytelnicy[czytelnik]) == 3
            


    def dodaj_ksiazke(ksiazka):
        if (ksiazka.tytul, ksiazka.autor,ksiazka.rok) not in biblioteka.ksiazki:
            biblioteka.ksiazki[(ksiazka.tytul,ksiazka.autor,ksiazka.rok)] = 1
        else:
            biblioteka.ksiazki[(ksiazka.tytul,ksiazka.autor, ksiazka.rok)] += 1
        return "True"
    
    def wypozycz_ksiazke(czytelnik, tytul):
        if not pobierz_czytelnika(czytelnik) and sprawdz_stan(tytul):
            self.czytelnicy[czytelnik][tytul] = 1
            return "True"
        else:
            return "False"
        if sprawdz_stan(tytul) and not sprawdz_czy_ta_sama(czytelnik, tytul) and not sprawdz_czy_trzy(czytelnik):
            self.czytelnicy[czytelnik][tytul] = 1
            return "True"
        else:
            return "False"

    def oddaj_ksiazke(czytelnik, tytul):
        if not pobierz_czytelnika(czytelnik):
            return "False"
        if tytul not in self.czytelnicy[czytelnilk]:
            return "False"
        else:
            del self.czytelnicy[czytelnik][tytul]
            return "True"




def main():
    liczba_akcji = input()
    biblioteka = Biblioteka({},{})

    for _ in range(int(liczba_akcji)):
        dane_wejsciowe = eval(input())
        print(dane_wejsciowe)

        if dane_wejsciowe[0] == "dodaj":
            ksiazka = Ksiazka(dane_wejsciowe[1], dane_wejsciowe[2], int(dane_wejsciowe[3]))
            wynik = biblioteka.dodaj_ksiazke(ksiazka)
        elif dane_wejsciowe[0] == "wypozycz":
            wynik = biblioteka.wypozycz_ksiazke(dane_wejsciowe[1], dane_wejsciowe[2])
        else:
            wynik =biblioteka.oddaj_ksiazke(dane_wejsciowe[1], dane_wejsciowe[2])
        print(wynik)

        

if __name__ == "__main__":
    main()
