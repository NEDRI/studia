# Zadanie 3 – prosty kalkulator
a = float(input("Podaj a: "))
b = float(input("Podaj b: "))

suma = a + b
roznica = a - b
iloczyn = a * b

print("Suma:", suma)
print("Różnica:", roznica)
print("Iloczyn:", iloczyn)

# Dzielenie przez zero powoduje wyjątek ZeroDivisionError i przerwanie programu,
# dlatego sprawdzamy b przed dzieleniem.
if b != 0:
    iloraz = a / b
    print("Iloraz:", iloraz)
else:
    print("Iloraz: nie można dzielić przez zero!")
