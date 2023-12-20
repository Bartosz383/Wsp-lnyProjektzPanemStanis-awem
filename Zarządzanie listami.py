tasks = []
def add_task(task):
    tasks.append(task)
    print(f"Dodano zadanie: {task}")
def remove_task(task):
    tasks.remove(task)
    print("Odjęto zadanie: ", task)
def show_task(task):
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    if tasks == []:
        print("[Ta lista jest pusta]")
while True:
    print("\nWybierz opcję:")
    print("1. Dodaj zadanie")
    print("2. Usuń zadanie")
    print("3. Wyświetl zadania")
    print("4. Wyjście")

    choice = input("Twój wybór: ")

    if choice == '1':
        task = input("Podaj nowe zadanie: ")
        add_task(task)
    elif choice == '2':
        task = input("Podaj zadanie do usunięcia: ")
        remove_task(task)
    elif choice == '3':
        show_task(tasks)
    elif choice == '4':
        print("Do widzenia!")
        break
    else:
        print("Nieprawidłowy wybór. Wybierz opcję od 1 do 4.")