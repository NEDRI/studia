# Lab1, Zadanie 8 – nazwa i adres IPv4 komputera z użyciem modułu socket
import socket

nazwa = socket.gethostname()

# Adres IPv4 aktywnego interfejsu: "łączymy" gniazdo UDP z adresem zewnętrznym
# (żaden pakiet nie jest wysyłany), system wybiera wtedy właściwy interfejs.
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.connect(("8.8.8.8", 80))
    ipv4 = s.getsockname()[0]
except OSError:
    ipv4 = socket.gethostbyname(nazwa)
finally:
    s.close()

# gethostbyaddr() – odwrotne odwzorowanie: adres IP -> (nazwa, aliasy, lista adresów)
try:
    host, aliasy, adresy = socket.gethostbyaddr(ipv4)
except (socket.herror, socket.gaierror):
    host, aliasy, adresy = nazwa, [], [ipv4]

print("Nazwa komputera:", nazwa)
print("Nazwa z gethostbyaddr():", host)
print("Adres IPv4:", ipv4)
print("Adresy z gethostbyaddr():", ", ".join(adresy))
