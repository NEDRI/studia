# Zadanie 2 – komunikacja z użytkownikiem
imie = input("Podaj imię: ")
wiek = input("Podaj wiek: ")

print("Typ wartości zwracanej przez input():", type(wiek))  # zawsze str

wiek = int(wiek)
print("Typ wieku po konwersji:", type(wiek))

print(f"Witaj {imie}!")
print(f"Masz {wiek} lat.")
