from time import sleep
import sys
import random
lista_klawiszy = {1: 'q', 2: 'w', 3: 'e', 4: 'r', 5: 't', 6: 'y', 7: 'u', 8: 'i', 9: 'o', 10: 'p',
                  11: 'a', 12: 's', 13: 'd', 14: 'f', 15: 'g', 16: 'h', 17: 'j', 18: 'k', 19: 'l',
                  20: 'z', 21: 'x', 22: 'c', 23: 'v', 24: 'b', 25: 'n', 26: 'm'}
klawisz_wygranej = random.choice in lista_klawiszy
wybrane_miejsca = random.choices in lista_klawiszy
wpis_gracza = input
ilosc_prob = 10
def head():
    line_1 = "Witaj w klawiaturowym saperze!"
    while True:
        def efekt_pisania():
            for x in line_1:
                print(x, end='')
                sys.stdout.flush()
                sleep(0.1)
        efekt_pisania()
        sleep(1.5)
        line_1 = "\nWpisz literę S aby zacząć: Literę Z żeby zobacyć zasady gry: Literę W aby wyjść z gry.\n"
        efekt_pisania()

        line_1_input = input()
        if line_1_input == "S":
            line_1 = "\n\nGra rozpoczyna się......"
            efekt_pisania()
            def rozgrywka():
                def przechodzenie_gry():
                    def wpis():
                        print("\n" * 100)
                        sleep(3)
                        print("Start!")
                        sleep(2)
                        print("\n" * 100)
                    def czas():
                        czasomierz = 60
                        while czasomierz > 0:
                            czasomierz = czasomierz - 1
                            sleep(1)
                            ilosc_prob = 10
                            if wpis_gracza != klawisz_wygranej or wybrane_miejsca:
                                ilosc_prob = ilosc_prob - 1
                                print("Źle! Próbuj dalej!")

                            elif wpis_gracza == wybrane_miejsca:
                                print("Wpadłeś w bombę klawiaturową, Przegrałeś!")
                                exit(99)
                            elif ilosc_prob == 0:
                                print("Skończyły ci się próby, Przegrałeś!")
                                exit(99)
                            elif wpis_gracza == klawisz_wygranej:
                                print("Brawo, znalazłeś wygrany klawisz!")
                        if czasomierz == 0:
                            print('Koniec czasu, przegrałeś!')
                            exit(99)


                    wpis()
                    czas()
                przechodzenie_gry()
            rozgrywka()
            exit(99)
        elif line_1_input == "Z":
            print("Klawiaturowy Saper: Zasady Gry: \nW tej grze, musisz odgadnąć przez komputer wybrany klawisz litery na twojej klawiaturze"
                  "\nJednak masz na to tylko 60 sekund czyli inaczej minutę aby odgadnąć dany klawisz"
                  "\nMasz tylko 10 prób, więc bądź uważny!"
                  "\nAle uwaga! Komputer wybrał także miejsc bomb klawiszowych! Jeśli wpiszesz klawisz na którym zjadnowała się bomba, koniec gry! Bomb klawiszowych jest 5"
                  "\nKomputer będzie zdolny ci dawać wskazówki. Będzie on także zdolny do mówienia czy twoja próba jest daleko, blisko bądź bardzo blisko do celu."
                  "\nZakres klawiszy jest od q do m. (Tylko alfabet)"
                  "\n\n Powodzenia!")
            exit(99)
        elif line_1_input == "W":
            print("Do Zobaczenia!")
            exit(99)
        else:
            print("Przepraszamy, lecz nie znaleziono takiej komendy.")
head()