from dataclasses import dataclass, field
import typing
import ast

@dataclass(frozen=True)
class Ksiazka:
    tytul: str
    autor: str
    rok: int

@dataclass(frozen=False)
class Czytelnik:
    imie: str
    wypozyczone: list = field(default_factory=list)

@dataclass(frozen=False)
class Biblioteka:
    ksiazki: typing.Dict[Ksiazka, int] = field(default_factory=dict) # slownik gdzie klucz to obiekt klasy Ksiazka a wartosc liczba egzemplarzy
    czytelnicy: typing.Dict[str, list] =field(default_factory=dict) # slownik z obiektami klasy Czytelnik


    def pobierz_czytelnika(self,czytelnik: Czytelnik) -> bool:
        if czytelnik.imie in self.czytelnicy:
            return True
        else:
            return False
    
    def sprawdz_stan(self,tytul_ksiazki: str) -> bool:
        for ksiazka, egzemplarze in self.ksiazki.items():
            if ksiazka.tytul == tytul_ksiazki:
                return egzemplarze > 0
        
        return False

    def ksiazka_po_tytule(self,tytul_ksiazki: str) -> Ksiazka:
        for ksiazka in self.ksiazki:
            if ksiazka.tytul == tytul_ksiazki:
                return ksiazka
    
    def sprawdz_czy_ta_sama(self,czytelnik: Czytelnik, tytul: str) -> bool:
        if czytelnik.imie in self.czytelnicy:
            if tytul in self.czytelnicy[czytelnik.imie]:
                    return True
        return False
    
    def sprawdz_czy_trzy(self,czytelnik: Czytelnik) -> bool:
        if czytelnik.imie in self.czytelnicy:
            return len(self.czytelnicy[czytelnik.imie]) > 2

            


    def dodaj_ksiazke(self,ksiazka: Ksiazka):
        if ksiazka not in self.ksiazki:
            self.ksiazki[ksiazka] = 1
        else:
            self.ksiazki[ksiazka] += 1
        return "True"
    
    def wypozycz_ksiazke(self,czytelnik: Czytelnik, tytul: str):
        if not self.pobierz_czytelnika(czytelnik) and self.sprawdz_stan(tytul):
            self.czytelnicy[czytelnik.imie] = [tytul]
            ksiazka = self.ksiazka_po_tytule(tytul)
            self.ksiazki[ksiazka] -= 1
            return "True"

        if self.sprawdz_stan(tytul) and not self.sprawdz_czy_ta_sama(czytelnik, tytul) and not self.sprawdz_czy_trzy(czytelnik):
            self.czytelnicy[czytelnik.imie].append(tytul)
            ksiazka = self.ksiazka_po_tytule(tytul)
            self.ksiazki[ksiazka] -= 1
            return "True"
        else:
            return "False"

    def oddaj_ksiazke(self,czytelnik: Czytelnik, tytul: str):
        if not self.pobierz_czytelnika(czytelnik):
            return "False"
        if tytul not in self.czytelnicy[czytelnik.imie]:
            return "False"
        else:
            ksiazka = self.ksiazka_po_tytule(tytul)
            self.ksiazki[ksiazka] += 1
            self.czytelnicy[czytelnik.imie].remove(tytul)  
            return "True"




def main():
    liczba_akcji = input()
    biblioteka = Biblioteka()

    for _ in range(int(liczba_akcji)):
        dane_wejsciowe = eval(input())
        if dane_wejsciowe[0] == "dodaj":
            ksiazka = Ksiazka(dane_wejsciowe[1], dane_wejsciowe[2], int(dane_wejsciowe[3]))
            wynik = biblioteka.dodaj_ksiazke(ksiazka)
        elif dane_wejsciowe[0] == "wypozycz":
            czytelnik = Czytelnik(dane_wejsciowe[1])
            wynik = biblioteka.wypozycz_ksiazke(czytelnik, dane_wejsciowe[2])
        else:
            czytelnik = Czytelnik(dane_wejsciowe[1])
            wynik = biblioteka.oddaj_ksiazke(czytelnik, dane_wejsciowe[2])
        print(wynik)

        

if __name__ == "__main__":
    main()
