from dataclasses import dataclass
from operator import itemgetter
import ast

@dataclass(frozen=True, order=True)
class Ksiazka:
    tytul: str
    autor: str
    rok: int

@dataclass(frozen=True, order=True)
class Biblioteka:
    ksiazki: dict()

    def stan_biblioteki(self):
        stan_lista = list()
        for (tytul, autor), egzemplarze in self.ksiazki.items():
            krotka = tytul,autor,egzemplarze
            stan_lista.append(krotka)
        return sorted(stan_lista, key=itemgetter(0))



def main():
    liczba_ksiazek = input()
    biblioteka = Biblioteka({})

    for _ in range(int(liczba_ksiazek)):
        dane_ksiazki = eval(input())
        ksiazka = Ksiazka(*dane_ksiazki)

        if (ksiazka.tytul, ksiazka.autor) not in biblioteka.ksiazki:
            biblioteka.ksiazki[(ksiazka.tytul,ksiazka.autor)] = 1
        else:
            biblioteka.ksiazki[(ksiazka.tytul,ksiazka.autor)] += 1
    stan = biblioteka.stan_biblioteki()
    for krotka in stan:
        print(krotka)
        

if __name__ == "__main__":
    main()
