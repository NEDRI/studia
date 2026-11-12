# Odpowiedzi do zadań – L0, Lab1, Lab2

---

## L0 – Wprowadzenie do Pythona (programy w `L0_wprowadzenie_python/`)

| Zadanie | Plik | Wynik testu |
|---|---|---|
| 1 | `L0_wprowadzenie_python/zad1.py` | `Nazywam się Jan i mam 20 lat.` |
| 2 | `L0_wprowadzenie_python/zad2.py` | Jan / 20 → `Witaj Jan!  Masz 20 lat.` |
| 3 | `L0_wprowadzenie_python/zad3.py` | 10 i 4 → 14, 6, 40, 2.5; b = 0 → komunikat zamiast błędu |
| 4 | `L0_wprowadzenie_python/zad4.py` | 60 → brak, 80 → brak, 95 → ostrzeżenie |
| 5 | `L0_wprowadzenie_python/zad5.py` | 11.5 → za niskie, 12 → OK, 13.8 → OK |
| 6 | `L0_wprowadzenie_python/zad6.py` | 70 → prawidłowa, 90 → podwyższona, 110 → ALARM |
| 7 | `L0_wprowadzenie_python/zad7.py` | 6000 → krytyczna, 4000 → wysoka, 1500 → prawidłowa, 0 → zatrzymany |

**Zad. 1**
- `imie` ma typ `str` (napis).
- `wiek` ma typ `int` (liczba całkowita).
- Po `wiek = "20"` zmienna ma typ `str`, bo cudzysłów oznacza napis. Python ma typowanie dynamiczne: typ wynika z wartości, a nie z deklaracji.

**Zad. 2:** `input()` zawsze zwraca `str`. Liczbę uzyskujemy przez `int(wiek)`.

**Zad. 3:** dzielenie przez zero zgłasza wyjątek `ZeroDivisionError: division by zero` i program się kończy. Dlatego program najpierw sprawdza, czy `b != 0`.

**Zad. 4**
- Dla 80 °C warunek `80 > 80` jest fałszywy, bo `>` to nierówność ostra.
- Żeby 80 °C też dawało ostrzeżenie, trzeba napisać `if temperatura >= 80:`.

**Zad. 6**
- 100 °C → „UWAGA – temperatura podwyższona” (100 > 100 jest fałszem, ale 100 > 80 prawdą).
- 80 °C → „Temperatura prawidłowa”.
- Kolejność ma znaczenie, bo `if/elif` wykonuje tylko pierwszy spełniony warunek. Gdyby `T > 80` stało na początku, dla 110 °C program wypisałby „UWAGA” zamiast „ALARM”. Najostrzejszy warunek musi być pierwszy.

---

## Lab1 – Protokoły komunikacyjne (folder `Lab1_siec/`)

Zadania 1–7 wykonuje się w `cmd` na komputerze w sali. Wartości zależą od stanowiska, więc trzeba je wpisać samemu. Poniżej jest opis, gdzie szukać każdej informacji.

### Zadanie 1 – `ipconfig`, `ipconfig /all`
| Co | Gdzie w wyniku |
|---|---|
| 1) Nazwa komputera | `Host Name` (`Nazwa hosta`) w sekcji *Windows IP Configuration* |
| 2) Aktywny interfejs | sekcja `Ethernet adapter …` / `Wireless LAN adapter …`, która ma adres IPv4 i **nie** ma `Media disconnected` |
| 3) Adres IPv4 | `IPv4 Address` |
| 4) Maska | `Subnet Mask`, np. 255.255.255.0 = /24 |
| 5) Brama | `Default Gateway` |
| 6) MAC | `Physical Address`, np. 4C-CF-7C-3A-A1-93 |
| 7) DNS | `DNS Servers` |
| 8) DHCP | `DHCP Enabled: Yes/No` |
| 9) Liczba interfejsów | liczba sekcji `… adapter …` (fizyczne i wirtualne, np. Hyper-V, VPN, Bluetooth) |

### Zadanie 2 – `getmac`
`getmac` wypisuje MAC (`Physical Address`) każdej karty razem z nazwą transportu (`\Device\Tcpip_{GUID}`). Adresy są takie same jak `Physical Address` w `ipconfig /all`. Przy kartach odłączonych pojawia się `Media disconnected`. `getmac` pokazuje same MAC, bez IP, maski i bramy.

### Zadanie 3 – `ping 127.0.0.1`, `ping WŁASNY_IP`
`127.0.0.1` to adres pętli zwrotnej (*loopback*, `localhost`, cała sieć 127.0.0.0/8). Pakiety nie wychodzą do sieci, tylko krążą wewnątrz stosu TCP/IP. Odpowiedzi z 127.0.0.1 oznaczają, że stos TCP/IP działa. Ping na własny adres IP sprawdza dodatkowo konfigurację interfejsu. Czasy wynoszą zwykle `<1 ms`, a TTL = 128 (domyślna wartość w Windows).

### Zadanie 4 – ping do sąsiada
Zapisz: `Reply from X: bytes=32 time=…ms TTL=…` oraz statystykę (`Sent/Received/Lost`, min/max/avg). Jeśli wychodzi `Request timed out`, to zwykle zapora Windows blokuje ICMP Echo na komputerze sąsiada. Nie oznacza to braku łączności (porównaj Lab2, zad. 4).

### Zadanie 5 – `arp -a` → ping → `arp -a`
Za drugim razem w tablicy pojawia się (albo odświeża) wpis `IP_sąsiada  MAC_sąsiada  dynamic`. Przed wysłaniem pakietu komputer musi poznać MAC odbiorcy w sieci lokalnej. Wysyła więc zapytanie ARP (broadcast „kto ma IP X?”), a odpowiedź trafia do pamięci podręcznej ARP. Adresy spoza podsieci nie trafiają do tablicy ARP. Dla nich zapisywany jest MAC bramy.

### Zadanie 6 – `tracert`
- `tracert IP_sąsiada` daje **1 przeskok**, bo sąsiad jest w tej samej podsieci i pakiety nie przechodzą przez router.
- `tracert 8.8.8.8` daje zwykle kilka do kilkunastu przeskoków. Pierwszy to brama domyślna. Wpisz liczbę z własnego wyniku. Gwiazdki `* * *` oznaczają routery, które nie odpowiadają na ICMP.

### Zadanie 7 – karta sieciowa
- PowerShell: `Get-NetAdapter | Format-List Name, InterfaceDescription, LinkSpeed, MacAddress, Status`
- `InterfaceDescription` to pełna nazwa, z której odczytasz producenta i model (np. *Intel(R) Ethernet Connection I219-LM*, *Realtek PCIe GbE Family Controller*).
- `LinkSpeed` to prędkość, np. 1 Gbps.
- To samo znajdziesz w Menedżerze urządzeń: *Karty sieciowe → Właściwości* (zakładki *Ogólne* i *Szczegóły*).

### Zadanie 8 – `Lab1_siec/zad8.py`
Program wypisuje nazwę komputera (`socket.gethostname()`) i adres IPv4 aktywnego interfejsu. Potem robi odwrotne zapytanie `socket.gethostbyaddr(ipv4)`, które zwraca krotkę `(nazwa_hosta, aliasy, lista_adresów)`. Wynik testu:
```
Nazwa komputera: eos
Nazwa z gethostbyaddr(): eos
Adres IPv4: 192.168.6.212
Adresy z gethostbyaddr(): 192.168.6.212
```

---

## Lab2 – Ethernet, TCP i UDP (programy w `Lab2_tcp_udp/`, uruchamiać z tego folderu)

| Rozdział | Pliki |
|---|---|
| 2. UDP | `udp_server.py`, `udp_client.py` |
| 3. TCP | `tcp_server.py`, `tcp_client.py` |
| 6. Mini-protokół | `protokol_server.py`, `protokol_client.py` |
| 7. Dwukierunkowa | `zad7_server.py`, `zad7_client.py` |
| 8. Obsługa błędów | `zad8_server.py`, `zad8_client.py` |
| 9. Wielu klientów | `zad9_server.py`, `zad9_client.py` |

**Rozdz. 2:** serwer wyświetla adres i port klienta, np. `('127.0.0.1', 54321)`. Port klienta to **port efemeryczny** przydzielany losowo przez system. Zmienia się przy każdym uruchomieniu klienta.

### 4. Komunikacja między stanowiskami
1. Sprawdź `ipconfig` na obu komputerach i wykonaj `ping` do sąsiada.
2. Na serwerze ustaw `HOST = "0.0.0.0"`, czyli nasłuchiwanie na wszystkich interfejsach. Przy `127.0.0.1` serwer jest dostępny tylko lokalnie.
3. W kliencie ustaw `SERVER_IP = "<IPv4 serwera>"`.
4. Uruchom najpierw serwer, potem klienta.
5. Powtórz dla TCP i zamieńcie się rolami.
6. Jeśli połączenia nie ma, to najczęściej blokuje je zapora Windows. Trzeba zezwolić Pythonowi na ruch w sieci prywatnej albo dodać regułę dla portów 5000/TCP i 5001/UDP. **Po zajęciach przywróć ustawienia zapory.**

Ping może nie działać (zapora blokuje ICMP), a TCP/UDP mimo to działa. To jest właśnie ta „wartościowa obserwacja” z instrukcji.

### 5. Zachowanie TCP i UDP
7. **Klient bez działającego serwera**
   - TCP: `connect()` od razu zgłasza `ConnectionRefusedError` (WinError 10061). Gdy host nie istnieje albo zapora odrzuca pakiety, pojawia się `TimeoutError` po kilku sekundach.
   - UDP: `sendto()` kończy się bez błędu, a klient czeka 3 s na `recvfrom()` i wypisuje „Brak odpowiedzi serwera.”. Klient UDP **nie wie**, czy ktoś odebrał datagram, bo protokół nie ma potwierdzeń.
   - Uwaga: w Windows na localhost `recvfrom()` może zgłosić `ConnectionResetError` (WinError 10054). System zamienia odebrany komunikat ICMP „port unreachable” na błąd. Nie robi tego UDP.
8. **Różne porty** – wynik jest taki sam jak w pkt 7. TCP od razu dostaje odmowę połączenia (pakiet RST), a UDP po cichu traci datagram i kończy się timeoutem. Sam adres IP wskazuje komputer, a dopiero port wskazuje aplikację.
9. **Zatrzymanie serwera w trakcie pracy**
   - TCP: system zamyka połączenie. `recv()` zwraca `b''` albo kolejne `send()` zgłasza `ConnectionResetError`/`BrokenPipeError`. Klient wie, że połączenie zostało zerwane.
   - UDP: klient dalej wysyła i dostaje tylko timeouty. Nie ma pojęcia połączenia, więc nie ma czego zrywać. Po restarcie serwera komunikacja wraca bez ponownego łączenia.
10. **Seria wiadomości**
    - TCP to **strumień bajtów**. Kilka szybko wysłanych `send()` może trafić do jednego `recv()` (np. `MSG1MSG2MSG3`), a duża wiadomość może się podzielić na kilka `recv()`. Kolejność bajtów jest zawsze zachowana.
    - Dlatego protokół musi sam oznaczać granice wiadomości: separator `\n` (tak robi `zad9_*`), stałą długość albo nagłówek z długością.
    - UDP zachowuje granice: jeden `sendto()` to jeden `recvfrom()`. Kolejność i dostarczenie nie są jednak gwarantowane (na localhost straty praktycznie nie występują).
11. **`netstat -an`**
    - Przed połączeniem TCP widać `TCP 127.0.0.1:5000 0.0.0.0:0 LISTENING`.
    - Po połączeniu dochodzą dwa wpisy `ESTABLISHED`: serwer :5000 ↔ klient :port_efemeryczny i odwrotnie.
    - Po zamknięciu połączenia widać `TIME_WAIT`.
    - UDP ma tylko wpis `UDP 127.0.0.1:5001 *:*` bez żadnego stanu, bo nie ma połączeń.
    - Filtrowanie wyniku: `netstat -an | findstr 500`

### 6. Mini-protokół – `protokol_server.py`
| Polecenie | Odpowiedź |
|---|---|
| `READ:TEMP` | `TEMP=23.7` |
| `READ:SPEED` | `SPEED=1450` |
| `READ:MOTOR` | `MOTOR=OFF` |
| `WRITE:MOTOR:ON`, `WRITE:MOTOR:OFF` | `ACK` |
| inne | `ERR:UNKNOWN_COMMAND` |

### 7. Komunikacja dwukierunkowa – `zad7_server.py`
| Polecenie | Odpowiedź |
|---|---|
| `READ:TEMP`, `READ:SPEED`, `READ:MOTOR`, `READ:ALARM` | `TEMP=…` / `SPEED=…` / `MOTOR=…` / `ALARM=0/1` |
| `READ:STATUS` | `MOTOR=ON;SPEED=1450;TEMP=24.1;ALARM=0` |
| `WRITE:MOTOR:ON/OFF` | `ACK:MOTOR=ON` albo `ERR:ALARM_ACTIVE`, gdy alarm jest aktywny |
| `WRITE:SPEED:<n>` | `ACK:SPEED=<n>` albo `ERR:INVALID_VALUE` |
| `RESET:ALARM` | `ACK:ALARM=0` |
| inne | `ERR:UNKNOWN_COMMAND` |

Serwer symuluje proces: włączony silnik podgrzewa urządzenie. Prędkość powyżej 3000 albo temperatura powyżej 80 °C włącza `ALARM=1`. Odpowiedź zależy od treści żądania i od stanu urządzenia, a klient reaguje na `ALARM=1` i `ERR`.

Przykładowa sesja (z testu):
```
Klient -> READ:TEMP          Serwer -> TEMP=23.5
Klient -> WRITE:MOTOR:ON     Serwer -> ACK:MOTOR=ON
Klient -> WRITE:SPEED:3500   Serwer -> ACK:SPEED=3500
Klient -> READ:STATUS        Serwer -> MOTOR=ON;SPEED=3500;TEMP=24.5;ALARM=1
Klient -> WRITE:MOTOR:ON     Serwer -> ERR:ALARM_ACTIVE
Klient -> RESET:ALARM        Serwer -> ACK:ALARM=0
```

### 8. Obsługa błędów – `zad8_server.py`, `zad8_client.py`
| Sytuacja | Jak wywołać | Reakcja |
|---|---|---|
| Serwer niedostępny | uruchom klienta bez serwera | `ConnectionRefusedError` albo `socket.timeout` → komunikat i ponowna próba co 3 s |
| Brak odpowiedzi w czasie | serwer zatrzymany (np. breakpoint) | `socket.timeout` (3 s) → ponowne połączenie |
| Niepoprawne polecenie | `BLA` | `ERR:UNKNOWN_COMMAND`, `ERR:UNKNOWN_PARAMETER` |
| Zły format | `WRITE:MOTOR`, `WRITE:MOTOR:XX`, `WRITE:SPEED:abc`, `READ:A:B` | `ERR:MISSING_VALUE`, `ERR:INVALID_VALUE`, `ERR:BAD_FORMAT` |
| Puste polecenie | Enter | klient nic nie wysyła |
| Zerwane połączenie | zabij klienta albo serwer | serwer: `ConnectionResetError` → czeka na nowego klienta; klient: `OSError` albo pusta odpowiedź → ponowne łączenie |
| Błędne kodowanie | wysłanie bajtów spoza UTF-8 | `UnicodeDecodeError` → `ERR:DECODE`, serwer działa dalej |

### 9. Wielu klientów – `zad9_server.py`, `zad9_client.py`
```bash
python zad9_server.py
python zad9_client.py SENSOR_1
python zad9_client.py ROBOT_2 192.168.x.y
python zad9_client.py PLC_3 127.0.0.1 1
```
- Każdy klient jest obsługiwany w osobnym wątku (`threading`). Wiadomości mają postać `ID;WARTOŚĆ\n`, bo separator `\n` wyznacza granice wiadomości w strumieniu TCP.
- Co 5 s serwer drukuje tabelę: ID, adres IP, wartość, czas ostatniej aktualizacji i stan (`OK` / `BRAK DANYCH (n s)` po 10 s bez danych / `ROZŁĄCZONY`).
- Rozszerzenie: wpisanie w konsoli serwera `ROBOT_2 SET:SPEED=1200` wysyła komendę do tego klienta. Klient ustawia prędkość i odsyła `ROBOT_2;ACK:SPEED=1200`.

### 10. Wnioski
- **TCP czy UDP?**
  - TCP wybieram tam, gdzie liczy się kompletność i kolejność danych: odczyt i zapis parametrów, receptury, komendy sterujące, konfiguracja (Modbus TCP, OPC UA, HTTP).
  - UDP wybieram do szybkich, cyklicznych danych, gdy następna próbka i tak zastąpi zgubioną: telemetria, streaming, wykrywanie urządzeń przez broadcast, PROFINET RT / EtherNet/IP I/O. Liczy się tu niski narzut i opóźnienie.
- **Najbardziej widoczna cecha TCP** to połączenie. Klient od razu wie, że serwer nie działa (`ConnectionRefused`) albo że połączenie zostało zerwane, a UDP tylko „milczy”. Drugą widoczną cechą jest strumieniowość: kilka wiadomości potrafi skleić się w jednym `recv()`.
- **Dlaczego sam IP nie wystarcza?** IP wskazuje komputer (interfejs), a na komputerze działa wiele aplikacji. Konkretny program wskazuje dopiero **port**. Para IP:port to gniazdo, a połączenie TCP jest opisane czwórką IP/port nadawcy i odbiorcy.
- **Co robić, gdy urządzenie przestaje odpowiadać?** Używać timeoutów zamiast czekać w nieskończoność. Ponawiać próby z odstępem, zgłaszać alarm i oznaczać dane jako nieaktualne (watchdog, tak jak `BRAK DANYCH` w zad. 9). Przejść w stan bezpieczny (np. zatrzymać silnik), a po powrocie urządzenia wznowić komunikację automatycznie.
- **Podobieństwo do protokołów przemysłowych**
  - Model żądanie–odpowiedź klient/serwer to master/slave w Modbus.
  - `READ`/`WRITE` + nazwa parametru odpowiadają kodom funkcji (FC03 Read Holding Registers, FC06 Write Single Register) i adresom rejestrów.
  - `ACK`/`ERR:…` odpowiadają odpowiedziom i kodom wyjątków Modbus (np. 01 Illegal Function, 03 Illegal Data Value).
  - Własny protokół jest tekstowy i bez sumy kontrolnej, a protokoły przemysłowe są binarne. Mają ramkę o ustalonej strukturze, nagłówek MBAP z długością i CRC (w Modbus RTU).
