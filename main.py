# tasks = []  # Lista zadań
#
# # Funkcja do dodawania zadania do listy
# def add_task(task):
#     tasks.append(task)
#     print(f"Dodano zadanie: {task}")
#
# # Funkcja do usuwania zadania z listy
# def remove_task(task):
#     if task in tasks:
#         tasks.remove(task)
#         print(f"Usunięto zadanie: {task}")
#     else:
#         print("Zadanie nie istnieje na liście.")
#
# # Funkcja do wyświetlania listy zadań
# def show_tasks():
#     if not tasks:
#         print("Lista zadań jest pusta.")
#     else:
#         print("Lista zadań:")
#         for index, task in enumerate(tasks, start=1):
#             print(f"{index}. {task}")
#
# # Pętla obsługująca interakcję z użytkownikiem
# while True:
#     print("\nWybierz opcję:")
#     print("1. Dodaj zadanie")
#     print("2. Usuń zadanie")
#     print("3. Wyświetl zadania")
#     print("4. Wyjście")
#
#     choice = input("Twój wybór: ")
#
#     if choice == '1':
#         task = input("Podaj nowe zadanie: ")
#         add_task(task)
#     elif choice == '2':
#         task = input("Podaj zadanie do usunięcia: ")
#         remove_task(task)
#     elif choice == '3':
#         show_tasks()
#     elif choice == '4':
#         print("Do widzenia!")
#         break
#     else:
#         print("Nieprawidłowy wybór. Wybierz opcję od 1 do 4.")

# import tkinter as tk
#
# tasks = []  # Lista zadań
#
# def add_task():
#     task = entry.get()
#     if task:
#         tasks.append(task)
#         update_task_list()
#
# def remove_task():
#     task = entry.get()
#     if task in tasks:
#         tasks.remove(task)
#         update_task_list()
#
# def show_tasks():
#     task_list.delete(0, tk.END)
#     if tasks:
#         for index, task in enumerate(tasks, start=1):
#             task_list.insert(tk.END, f"{index}. {task}")
#     else:
#         task_list.insert(tk.END, "Lista zadań jest pusta.")
#
# def update_task_list():
#     show_tasks()
#     entry.delete(0, tk.END)
#
# root = tk.Tk()
# root.title("Prosty menedżer zadań")
#
# frame = tk.Frame(root)
# frame.pack(padx=80, pady=0)
#
# label = tk.Label(frame, text="Dodaj lub usuń zadanie:")
# label.pack()
#
# entry = tk.Entry(frame)
# entry.pack()
#
# add_button = tk.Button(frame, text="Dodaj zadanie", command=add_task)
# add_button.pack(pady=5)
#
# remove_button = tk.Button(frame, text="Usuń zadanie", command=remove_task)
# remove_button.pack(pady=5)
#
# task_list = tk.Listbox(frame, width=40, height=10)
# task_list.pack(pady=10)
#
# show_tasks()
#
# root.mainloop()


import time
import sys
import random
import threading
# lista_klawiszy = {1: 'q', 2: 'w', 3: 'e', 4: 'r', 5: 't', 6: 'y', 7: 'u', 8: 'i', 9: 'o', 10: 'p',
#                  11: 'a', 12: 's', 13: 'd', 14: 'f', 15: 'g', 16: 'h', 17: 'j', 18: 'k', 19: 'l',
#                  20: 'z', 21: 'x', 22: 'c', 23: 'v', 24: 'b', 25: 'n', 26: 'm'}
lista_klawiszy = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
klawisz_wygranej = random.choice(lista_klawiszy)
wybrane_miejsca = random.choice(lista_klawiszy)
ilosc_prob = 10

class CountdownThread(threading.Thread):
    def __init__(self, start_value):
        super(CountdownThread, self).__init__()
        self.start_value = start_value

    def run(self):
        for i in range(self.start_value, 0, -1):
            print("\n")
            print(i)
            time.sleep(1)
            #break
          #  exit(99)

# def czas():
#     global start_time
#     czasomierz = 5
#     while czasomierz > 0:
#         elapsed_time = int(time.time() - start_time)
#         czasomierz = 5 - elapsed_time
#         print(f"Czas: {czasomierz} sekund")
#
#         if czasomierz == 0:
#          print('Koniec czasu, przegrałeś!')
#          exit(99)
    # czasomierz = czasomierz - 1
    # sleep(1)
    # print(f"Czas: {czasomierz} sekund")
    # if czasomierz == 0:
    #     print('Koniec czasu, przegrałeś!')
    #     exit(99)


def wpis():
    print("\n" * 100)
    # sleep(3)
    print("Start!")
    # sleep(2)
    print("\n" * 100)
    print(klawisz_wygranej)
    print(wybrane_miejsca)
    print(lista_klawiszy)


def ilosc_prod():
    ilosc_prob = 10
    thread = CountdownThread(5)
    thread.start()

    while True:
        wpis_gracza = input("Wpisz literę: ")


        if wpis_gracza == wybrane_miejsca:
            ilosc_prob = ilosc_prob - 1
            print(f"Pozostałe próby: {ilosc_prob}")
            print("Wpadłeś w bombę klawiaturową, Przegrałeś!")
            break

        elif wpis_gracza != klawisz_wygranej:
            ilosc_prob = ilosc_prob - 1
            print("Źle! Próbuj dalej!")
            print(f"Pozostałe próby: {ilosc_prob}")

            if ilosc_prob == 0:
                print("Skończyły ci się próby, Przegrałeś!")
                break

        elif wpis_gracza == klawisz_wygranej:
            print("Brawo, znalazłeś wygrany klawisz!")
            break
def main():
    line_1 = "Witaj w klawiaturowym saperze!"
    while True:
        def efekt_pisania():
            for x in line_1:
                print(x, end='')
                #sys.stdout.flush()
                #sleep(0.1)
        efekt_pisania()
        #sleep(1.5)
        line_1 = "\nWpisz literę S aby zacząć: Literę Z żeby zobacyć zasady gry: Literę W aby wyjść z gry.\n"
        efekt_pisania()

        line_1_input = input()
        if line_1_input == "S":
            line_1 = "\n\nGra rozpoczyna się......"
            efekt_pisania()

            wpis()
            ilosc_prod()
            break

        elif line_1_input == "Z":
            print("Klawiaturowy Saper: Zasady Gry: \nW tej grze, musisz odgadnąć przez komputer wybrany klawisz litery na twojej klawiaturze"
                  "\nJednak masz na to tylko 60 sekund czyli inaczej minutę aby odgadnąć dany klawisz"
                  "\nMasz tylko 10 prób, więc bądź uważny!"
                  "\nAle uwaga! Komputer wybrał także miejsc bomb klawiszowych! Jeśli wpiszesz klawisz na którym zjadnowała się bomba, koniec gry! Bomb klawiszowych jest 5"
                  "\nKomputer będzie zdolny ci dawać wskazówki. Będzie on także zdolny do mówienia czy twoja próba jest daleko, blisko bądź bardzo blisko do celu."
                  "\nZakres klawiszy jest od q do m. (Tylko alfabet)"
                  "\n\n Powodzenia!")
            break
        elif line_1_input == "W":
            print("Do Zobaczenia!")
            break
        else:
            print("Przepraszamy, lecz nie znaleziono takiej komendy.")

if __name__ == "__main__":
    main()
