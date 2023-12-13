Wpis = input("Wpisz dowolne zdanie/ słowo a ja sprawdzę czy to palindrom. \n")
if Wpis[::-1] == Wpis:
    print("Twoje słowo/zdanie jest palindromem.")
else:
    print("Twoje słowo/zdanie nie jest palindromem")