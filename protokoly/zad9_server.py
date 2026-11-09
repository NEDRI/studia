# Lab2, Zadanie 9 – serwer TCP obsługujący wielu klientów (threading)
#
# Format danych od klienta (jedna wiadomość = jedna linia zakończona \n):
#     SENSOR_1;TEMP=23.4
#     ROBOT_2;STATE=RUN
#     PLC_3;COUNTER=128
#     ROBOT_2;ACK:SPEED=1200        <- potwierdzenie komendy sterującej
#
# Konsola serwera: "<ID> <komenda>" wysyła komendę sterującą do klienta,
# np.  ROBOT_2 SET:SPEED=1200
import socket
import threading
import time
from datetime import datetime

HOST = "0.0.0.0"
PORT = 5002
STALE_AFTER = 10      # [s] brak nowych danych dłużej niż tyle -> "BRAK DANYCH"
TABLE_EVERY = 5       # [s] co ile odświeżać tabelę

devices = {}          # ID -> {"addr", "value", "time", "conn"}
lock = threading.Lock()


def handle_client(conn, addr):
    device_id = None
    buffer = ""
    print(f"[+] Połączono z {addr[0]}:{addr[1]}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            buffer += data.decode("utf-8", errors="replace")
            # TCP to strumień – dzielimy go na wiadomości po znaku \n
            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)
                line = line.strip()
                if not line:
                    continue
                if ";" not in line:
                    conn.sendall(b"ERR:BAD_FORMAT\n")
                    continue
                device_id, value = line.split(";", 1)
                if value.startswith(("ACK", "ERR")):
                    print(f"[{device_id}] odpowiedź na komendę: {value}")
                    continue
                with lock:
                    devices[device_id] = {
                        "addr": addr[0],
                        "value": value,
                        "time": time.time(),
                        "conn": conn,
                    }
                conn.sendall(b"ACK\n")
    except (ConnectionResetError, OSError) as error:
        print(f"[!] Błąd połączenia z {addr}: {error}")
    finally:
        conn.close()
        with lock:
            if device_id in devices:
                devices[device_id]["conn"] = None
        print(f"[-] Rozłączono {device_id or addr}")


def print_table():
    while True:
        time.sleep(TABLE_EVERY)
        now = time.time()
        with lock:
            rows = sorted(devices.items())
        print()
        print(f"{'ID urządzenia':<14}{'Adres IP':<16}{'Wartość':<26}{'Ostatnia aktualizacja':<23}Stan")
        print("-" * 91)
        for dev_id, d in rows:
            age = now - d["time"]
            if d["conn"] is None:
                state = "ROZŁĄCZONY"
            elif age > STALE_AFTER:
                state = f"BRAK DANYCH ({age:.0f} s)"
            else:
                state = "OK"
            last = datetime.fromtimestamp(d["time"]).strftime("%H:%M:%S")
            print(f"{dev_id:<14}{d['addr']:<16}{d['value']:<26}{last:<23}{state}")
        if not rows:
            print("(brak urządzeń)")
        print()


def console():
    """Wysyłanie komend sterujących: '<ID> <komenda>'."""
    while True:
        try:
            line = input().strip()
        except EOFError:
            return
        if " " not in line:
            continue
        dev_id, command = line.split(" ", 1)
        with lock:
            conn = devices.get(dev_id, {}).get("conn")
        if conn is None:
            print(f"Nie ma połączonego urządzenia {dev_id}")
            continue
        try:
            conn.sendall((command + "\n").encode("utf-8"))
            print(f"Wysłano do {dev_id}: {command}")
        except OSError as error:
            print("Błąd wysyłania:", error)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()
print(f"Serwer wielu klientów nasłuchuje na {HOST}:{PORT}")
print("Komenda sterująca: <ID> <komenda>, np. ROBOT_2 SET:SPEED=1200")

threading.Thread(target=print_table, daemon=True).start()
threading.Thread(target=console, daemon=True).start()

try:
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
except KeyboardInterrupt:
    print("\nZatrzymano serwer")
finally:
    server.close()
