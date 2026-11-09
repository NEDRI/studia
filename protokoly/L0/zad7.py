# Zadanie 7 – system kontroli prędkości obrotowej
n = float(input("Podaj prędkość obrotową n [obr/min]: "))

if n > 5000:
    print("Prędkość krytyczna")
elif n > 3000:
    print("Wysoka prędkość")
elif n > 0:
    print("Praca prawidłowa")
else:
    print("Silnik zatrzymany")
