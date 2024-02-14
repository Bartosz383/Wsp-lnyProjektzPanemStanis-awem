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

#
# import time
# import sys
# import random
# import threading
# # lista_klawiszy = {1: 'q', 2: 'w', 3: 'e', 4: 'r', 5: 't', 6: 'y', 7: 'u', 8: 'i', 9: 'o', 10: 'p',
# #                  11: 'a', 12: 's', 13: 'd', 14: 'f', 15: 'g', 16: 'h', 17: 'j', 18: 'k', 19: 'l',
# #                  20: 'z', 21: 'x', 22: 'c', 23: 'v', 24: 'b', 25: 'n', 26: 'm'}
# lista_klawiszy = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
# klawisz_wygranej = random.choice(lista_klawiszy)
# wybrane_miejsca = random.choice(lista_klawiszy)
# ilosc_prob = 10
#
# class CountdownThread(threading.Thread):
#     def __init__(self, start_value):
#         super(CountdownThread, self).__init__()
#         self.start_value = start_value
#
#     def run(self):
#         for i in range(self.start_value, 0, -1):
#             print("\n")
#             print(i)
#             time.sleep(1)
#             #break
#           #  exit(99)
#
# # def czas():
# #     global start_time
# #     czasomierz = 5
# #     while czasomierz > 0:
# #         elapsed_time = int(time.time() - start_time)
# #         czasomierz = 5 - elapsed_time
# #         print(f"Czas: {czasomierz} sekund")
# #
# #         if czasomierz == 0:
# #          print('Koniec czasu, przegrałeś!')
# #          exit(99)
#     # czasomierz = czasomierz - 1
#     # sleep(1)
#     # print(f"Czas: {czasomierz} sekund")
#     # if czasomierz == 0:
#     #     print('Koniec czasu, przegrałeś!')
#     #     exit(99)
#
#
# def wpis():
#     print("\n" * 100)
#     # sleep(3)
#     print("Start!")
#     # sleep(2)
#     print("\n" * 100)
#     print(klawisz_wygranej)
#     print(wybrane_miejsca)
#     print(lista_klawiszy)
#
#
# def ilosc_prod():
#     ilosc_prob = 10
#     thread = CountdownThread(5)
#     thread.start()
#
#     while True:
#         wpis_gracza = input("Wpisz literę: ")
#
#
#         if wpis_gracza == wybrane_miejsca:
#             ilosc_prob = ilosc_prob - 1
#             print(f"Pozostałe próby: {ilosc_prob}")
#             print("Wpadłeś w bombę klawiaturową, Przegrałeś!")
#             break
#
#         elif wpis_gracza != klawisz_wygranej:
#             ilosc_prob = ilosc_prob - 1
#             print("Źle! Próbuj dalej!")
#             print(f"Pozostałe próby: {ilosc_prob}")
#
#             if ilosc_prob == 0:
#                 print("Skończyły ci się próby, Przegrałeś!")
#                 break
#
#         elif wpis_gracza == klawisz_wygranej:
#             print("Brawo, znalazłeś wygrany klawisz!")
#             break
# def main():
#     line_1 = "Witaj w klawiaturowym saperze!"
#     while True:
#         def efekt_pisania():
#             for x in line_1:
#                 print(x, end='')
#                 #sys.stdout.flush()
#                 #sleep(0.1)
#         efekt_pisania()
#         #sleep(1.5)
#         line_1 = "\nWpisz literę S aby zacząć: Literę Z żeby zobacyć zasady gry: Literę W aby wyjść z gry.\n"
#         efekt_pisania()
#
#         line_1_input = input()
#         if line_1_input == "S":
#             line_1 = "\n\nGra rozpoczyna się......"
#             efekt_pisania()
#
#             wpis()
#             ilosc_prod()
#             break
#
#         elif line_1_input == "Z":
#             print("Klawiaturowy Saper: Zasady Gry: \nW tej grze, musisz odgadnąć przez komputer wybrany klawisz litery na twojej klawiaturze"
#                   "\nJednak masz na to tylko 60 sekund czyli inaczej minutę aby odgadnąć dany klawisz"
#                   "\nMasz tylko 10 prób, więc bądź uważny!"
#                   "\nAle uwaga! Komputer wybrał także miejsc bomb klawiszowych! Jeśli wpiszesz klawisz na którym zjadnowała się bomba, koniec gry! Bomb klawiszowych jest 5"
#                   "\nKomputer będzie zdolny ci dawać wskazówki. Będzie on także zdolny do mówienia czy twoja próba jest daleko, blisko bądź bardzo blisko do celu."
#                   "\nZakres klawiszy jest od q do m. (Tylko alfabet)"
#                   "\n\n Powodzenia!")
#             break
#         elif line_1_input == "W":
#             print("Do Zobaczenia!")
#             break
#         else:
#             print("Przepraszamy, lecz nie znaleziono takiej komendy.")
#
# if __name__ == "__main__":
#     main()

#
# import tkinter as tk
# from tkinter import scrolledtext, filedialog
# from PIL import Image, ImageTk
# import random
#
# def add_numbers():
#     try:
#         num1 = float(entry1.get())
#         num2 = float(entry2.get())
#         result = num1 + num2
#         text_area.insert(tk.END, f"{num1} + {num2} = {result}\n")
#     except ValueError:
#         text_area.insert(tk.END, "Błąd! Wprowadź poprawne liczby.\n")
#
# def subtract_numbers():
#     try:
#         num1 = float(entry1.get())
#         num2 = float(entry2.get())
#         result = num1 - num2
#         text_area.insert(tk.END, f"{num1} - {num2} = {result}\n")
#     except ValueError:
#         text_area.insert(tk.END, "Błąd! Wprowadź poprawne liczby.\n")
#
# def multiply_numbers():
#     try:
#         num1 = float(entry1.get())
#         num2 = float(entry2.get())
#         result = num1 * num2
#         text_area.insert(tk.END, f"{num1} * {num2} = {result}\n")
#     except ValueError:
#         text_area.insert(tk.END, "Błąd! Wprowadź poprawne liczby.\n")
#
# def divide_numbers():
#     try:
#         num1 = float(entry1.get())
#         num2 = float(entry2.get())
#         if num2 == 0:
#             raise ValueError("Nie można dzielić przez zero.")
#         result = num1 / num2
#         text_area.insert(tk.END, f"{num1} / {num2} = {result}\n")
#     except ValueError as e:
#         text_area.insert(tk.END, f"Błąd! {str(e)}\n")
#
# def browse_image():
#     file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
#     if file_path:
#         display_image(file_path)
#
# def display_image(image_path):
#     image = Image.open(image_path)
#     image = image.resize((200, 200), Image.ANTIALIAS)  # Adjust the size as needed
#     imgtk = ImageTk.PhotoImage(image)
#     image_label.config(image=imgtk)
#     image_label.image = imgtk
#
# def save_text():
#     text_to_save = text_area.get("1.0", tk.END)
#     file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
#     if file_path:
#         with open(file_path, "w") as file:
#             file.write(text_to_save)
#
# def open_text_file():
#     file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
#     if file_path:
#         with open(file_path, "r") as file:
#             content = file.read()
#             text_area.delete("1.0", tk.END)
#             text_area.insert(tk.END, content)
#
# import tkinter as tk
# from tkinter import scrolledtext, filedialog
# from PIL import Image, ImageTk
# import random
#
# def add_numbers():
#     try:
#         num1 = float(entry1.get())
#         num2 = float(entry2.get())
#         result = num1 + num2
#         text_area.insert(tk.END, f"{num1} + {num2} = {result}\n")
#     except ValueError:
#         text_area.insert(tk.END, "Błąd! Wprowadź poprawne liczby.\n")
#
# def subtract_numbers():
#     try:
#         num1 = float(entry1.get())
#         num2 = float(entry2.get())
#         result = num1 - num2
#         text_area.insert(tk.END, f"{num1} - {num2} = {result}\n")
#     except ValueError:
#         text_area.insert(tk.END, "Błąd! Wprowadź poprawne liczby.\n")
#
# def multiply_numbers():
#     try:
#         num1 = float(entry1.get())
#         num2 = float(entry2.get())
#         result = num1 * num2
#         text_area.insert(tk.END, f"{num1} * {num2} = {result}\n")
#     except ValueError:
#         text_area.insert(tk.END, "Błąd! Wprowadź poprawne liczby.\n")
#
# def divide_numbers():
#     try:
#         num1 = float(entry1.get())
#         num2 = float(entry2.get())
#         if num2 == 0:
#             raise ValueError("Nie można dzielić przez zero.")
#         result = num1 / num2
#         text_area.insert(tk.END, f"{num1} / {num2} = {result}\n")
#     except ValueError as e:
#         text_area.insert(tk.END, f"Błąd! {str(e)}\n")
#
# def browse_image():
#     file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
#     if file_path:
#         display_image(file_path)
#
# def display_image(image_path):
#     image = Image.open(image_path)
#     image = image.resize((200, 200), Image.ANTIALIAS)  # Adjust the size as needed
#     imgtk = ImageTk.PhotoImage(image)
#     image_label.config(image=imgtk)
#     image_label.image = imgtk
#
# def save_text():
#     text_to_save = text_area.get("1.0", tk.END)
#     file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
#     if file_path:
#         with open(file_path, "w") as file:
#             file.write(text_to_save)
#
# def open_text_file():
#     file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
#     if file_path:
#         with open(file_path, "r") as file:
#             content = file.read()
#             text_area.delete("1.0", tk.END)
#             text_area.insert(tk.END, content)
#
# def cool_function():
#     colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
#     random_color = random.choice(colors)
#     root.configure(bg=random_color)
#
# def reset_function():
#     root.configure(bg="black")
#     text_area.delete("1.0", tk.END)
#
# # Utwórz główne okno
# root = tk.Tk()
# root.title("Kalkulator Dodawania, Odejmowania, Mnożenia, Dzielenia i Wyświetlania Obrazu")
# root.configure(bg="black")
#
# # Utwórz etykiety i pola do wprowadzania liczb
# label1 = tk.Label(root, text="Liczba 1:", fg="white", bg="black")
# label1.pack(pady=5)
#
# entry1 = tk.Entry(root, bg="white")
# entry1.pack(pady=5)
#
# label2 = tk.Label(root, text="Liczba 2:", fg="white", bg="black")
# label2.pack(pady=5)
#
# entry2 = tk.Entry(root, bg="white")
# entry2.pack(pady=5)
#
# # Utwórz przyciski "Dodaj", "Odejmij", "Pomnóż" i "Podziel"
# add_button = tk.Button(root, text="Dodaj", command=add_numbers, bg="white")
# add_button.pack(pady=5)
#
# subtract_button = tk.Button(root, text="Odejmij", command=subtract_numbers, bg="white")
# subtract_button.pack(pady=5)
#
# multiply_button = tk.Button(root, text="Pomnóż", command=multiply_numbers, bg="white")
# multiply_button.pack(pady=5)
#
# divide_button = tk.Button(root, text="Podziel", command=divide_numbers, bg="white")
# divide_button.pack(pady=5)
#
# # Utwórz przyciski "Wybierz obraz", "Zapisz tekst", "Otwórz plik tekstowy", "Fajna Funkcja" i "Reset"
# browse_button = tk.Button(root, text="Wybierz obraz", command=browse_image, bg="white")
# browse_button.pack(pady=5)
#
# save_button = tk.Button(root, text="Zapisz tekst", command=save_text, bg="white")
# save_button.pack(pady=5)
#
# open_button = tk.Button(root, text="Otwórz plik tekstowy", command=open_text_file, bg="white")
# open_button.pack(pady=5)
#
# cool_function_button = tk.Button(root, text="Fajna Funkcja", command=cool_function, bg="white")
# cool_function_button.pack(pady=5)
#
# reset_button = tk.Button(root, text="Reset", command=reset_function, bg="white")
# reset_button.pack(pady=5)
#
# # Utwórz obszar do wyświetlania obrazu
# image_label = tk.Label(root, bg="white")
# image_label.pack(pady=10)
#
# # Utwórz obszar tekstowy
# text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10, bg="white")
# text_area.pack(pady=10)
#
# # Uruchamia pętlę główną
# root.mainloop()
#
#
# import tkinter as tk
# from tkinter import messagebox
# import random
#
# class TaskManager:
#     def __init__(self, root):
#         root.configure(bg="white")
#         self.root = root    # okienko
#         self.root.title("Task Manager")     # nazwa okienka
#
#         self.tasks = []     # początkowa lista zadań
#
#         # Tworzenie interfejsu użytkownika
#         self.label = tk.Label(root, text="Dodaj nowe zadanie:")
#         self.label.pack(pady=10)
#
#         self.entry = tk.Entry(root, width=40)
#         self.entry.pack(pady=10)
#
#         self.add_button = tk.Button(root, text="Dodaj zadanie", command=self.add_task)
#         self.add_button.pack(pady=5)
#
#         self.remove_button = tk.Button(root, text="Usuń zadanie", command=self.remove_task)
#         self.remove_button.pack(pady=5)
#
#         self.show_button = tk.Button(root, text="Wyświetl zadania", command=self.show_tasks)
#         self.show_button.pack(pady=10)
#
#         self.save_button = tk.Button(root, text="Zapisz do pliku", command=self.save_to_file)
#         self.save_button.pack(pady=5)
#
#         self.load_button = tk.Button(root, text="Wczytaj z pliku", command=self.load_from_file)
#         self.load_button.pack(pady=5)
#
#         self.color_button = tk.Button(root, text="Zmień kolor", command=self.change_color)
#         self.color_button.pack(pady=5)
#
#     def add_task(self):
#         task = self.entry.get()
#         if task:
#             self.tasks.append(task)
#             messagebox.showinfo("Sukces", f"Dodano zadanie: {task}")    # informacja w okienku, alert
#             self.entry.delete(0, tk.END)
#         else:
#             messagebox.showwarning("Błąd", "Wprowadź treść zadania!")
#
#     def remove_task(self):
#         if self.tasks:
#             selected_task = messagebox.askokcancel("Usuń zadanie", "Czy na pewno chcesz usunąć ostatnie zadanie?")
#             if selected_task:
#                 removed_task = self.tasks.pop()
#                 messagebox.showinfo("Sukces", f"Usunięto zadanie: {removed_task}")
#         else:
#             messagebox.showwarning("Błąd", "Brak zadań do usunięcia!")
#
#     def show_tasks(self):
#         if self.tasks:
#             tasks_text = "\n".join(self.tasks)
#             messagebox.showinfo("Lista zadań", f"Aktualne zadania:\n{tasks_text}")
#         else:
#             messagebox.showinfo("Lista zadań", "Brak zadań do wyświetlenia.")
#
#     def save_to_file(self):
#         if self.tasks:
#             filename = "tasks.txt" # nazwa pliku
#             with open(filename, "w", encoding='utf-8') as file:     # otwórz plik   # napisz w pliku i zapisz
#                 for task in self.tasks:
#                     file.write(task + "\n")
#             messagebox.showinfo("Sukces", f"Zapisano zadania do pliku: {filename}")
#         else:
#             messagebox.showwarning("Błąd", "Brak zadań do zapisania!")
#
#     def load_from_file(self):
#         try:
#             filename = "tasks.txt"
#             with open(filename, "r", encoding='utf-8') as file:
#                 lines = file.readlines()
#                 self.tasks = [line.strip() for line in lines]
#             messagebox.showinfo("Sukces", f"Wczytano zadania z pliku: {filename}")
#         except FileNotFoundError:
#             messagebox.showwarning("Błąd", f"Plik {filename} nie istnieje.")
#         except Exception as e:
#             messagebox.showwarning("Błąd", f"Wystąpił błąd podczas wczytywania z pliku:\n{str(e)}")
#
#     def change_color(self):
#         list_of_colors = ["maroon", "red", "orange", "yellow", "green", "cyan", "blue",
#                           "pink", "purple", "brown",
#                           "white", "grey", "black"]
#         root.configure(bg=random.choice(list_of_colors))
#         color_root = tk.Tk()
#         self.root = color_root
#         self.root.title = ("Wybierz kolor tła:")
#
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = TaskManager(root)
#     root.mainloop()


import random



slowa = ["kot", "pies", "chomik", "ptak", "szczur", "królik", "rybka", "świnia", "krowa", "kura", "koń", "owca"]
wybrane_slowo = random.choice(slowa)
print(wybrane_slowo)
def gra_w_wisielca():
    print("Odgadnij moje słowo: \nKategoria to zwierzęta domowe/hodowlane.")
    if input() == wybrane_slowo:
        print("Brawo, odgadłeś słowo!")
    else:
        print("Zła odpowiedź! Kreska narysowana, masz jeszcze 10 prób")
        if input() == wybrane_slowo:
            print("Brawo, odgadłeś słowo!")
        else:
            print("Zła odpowiedź! Kreska narysowana, masz jeszcze 9 prób")
            if input() == wybrane_slowo:
                print("Brawo, odgadłeś słowo!")
            else:
                print("Zła odpwiedź! Kreska narysowana, masz jeszcze 8 prób")
                if input() == wybrane_slowo:
                    print("Brawo, odgadłeś słowo!")
                else:
                    print("Zła odpwiedź! Kreska narysowana, masz jeszcze 7 prób")
                    if input() == wybrane_slowo:
                        print("Brawo, odgadłeś słowo!")
                    else:
                        print("Zła odpwiedź! Kreska narysowana, masz jeszcze 6 prób")
                        if input() == wybrane_slowo:
                            print("Brawo, odgadłeś słowo!")
                        else:
                            print("Zła odpwiedź! Kreska narysowana, masz jeszcze 5 prób")
                            if input() == wybrane_slowo:
                                print("Brawo, odgadłeś słowo!")
                            else:
                                print("Zła odpwiedź! Kreska narysowana, masz jeszcze 4 próby")
                                if input() == wybrane_slowo:
                                    print("Brawo, odgadłeś słowo!")
                                else:
                                    print("Zła odpwiedź! Kreska narysowana, masz jeszcze 3 próby")
                                    if input() == wybrane_slowo:
                                        print("Brawo, odgadłeś słowo!")
                                    else:
                                        print("Zła odpwiedź! Kreska narysowana, masz jeszcze 2 próby")
                                        if input() == wybrane_slowo:
                                            print("Brawo, odgadłeś słowo!")
                                        else:
                                            print("Zła odpwiedź! Kreska narysowana, masz jeszcze 1 próbę")
                                            if input() == wybrane_slowo:
                                                print("Brawo, odgadłeś słowo!")
                                            else:
                                                print("Przegrałeś, powieszono cię! :(")


if __name__ == "__main__":
    print("Witaj w grze w wisielca!")
    gra_w_wisielca()
