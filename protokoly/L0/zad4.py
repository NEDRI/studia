# Zadanie 4 – instrukcja if
temperatura = float(input("Podaj temperaturę urządzenia [°C]: "))

if temperatura > 80:
    print("UWAGA! Przekroczono dopuszczalną temperaturę.")

# Dla 80°C warunek 80 > 80 jest fałszywy. Aby 80°C też dawało ostrzeżenie,
# należy użyć warunku: if temperatura >= 80:
