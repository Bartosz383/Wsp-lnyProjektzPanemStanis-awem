def odszyfruj(wiadomosc, przesuniecie):
  odszyfrowana = ""
  for znak in wiadomosc:
    if znak.isalpha():
      odszyfrowana += chr((ord(znak) - przesuniecie) % 26 + ord("A"))
    else:
      odszyfrowana += znak
  return odszyfrowana

wiadomosc = "QWERTYUIOPASDFGHJKLZXCVBNM"
przesuniecie = 3

print(odszyfruj(wiadomosc, przesuniecie))