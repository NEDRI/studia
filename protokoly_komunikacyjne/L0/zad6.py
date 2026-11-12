# Zadanie 6 – instrukcja if...elif...else
T = float(input("Podaj temperaturę urządzenia T [°C]: "))

if T > 100:
    print("ALARM – temperatura krytyczna")
elif T > 80:
    print("UWAGA – temperatura podwyższona")
else:
    print("Temperatura prawidłowa")
