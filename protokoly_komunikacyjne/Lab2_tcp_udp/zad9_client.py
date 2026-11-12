# Lab2, Zadanie 9 – klient cyklicznie wysyłający dane procesowe
#
# Uruchomienie:  python zad9_client.py <ID> [IP_SERWERA] [OKRES_S]
#   python zad9_client.py SENSOR_1
#   python zad9_client.py ROBOT_2 192.168.1.20
#   python zad9_client.py PLC_3 127.0.0.1 1
import random
import socket
import sys
import threading
import time

DEVICE_ID = sys.argv[1] if len(sys.argv) > 1 else "SENSOR_1"
SERVER_IP = sys.argv[2] if len(sys.argv) > 2 else "127.0.0.1"
PERIOD = float(sys.argv[3]) if len(sys.argv) > 3 else 2.0
PORT = 5002

state = {"temp": 23.0, "counter": 0, "robot": "RUN", "speed": 1000}


def measurement():
    """Symulowana wartość procesowa zależna od typu urządzenia."""
    if DEVICE_ID.startswith("SENSOR"):
        state["temp"] = round(state["temp"] + random.uniform(-0.5, 0.5), 1)
        return f"TEMP={state['temp']}"
    if DEVICE_ID.startswith("ROBOT"):
        if random.random() < 0.2:
            state["robot"] = random.choice(["RUN", "STOP", "IDLE"])
        return f"STATE={state['robot']};SPEED={state['speed']}"
    state["counter"] += random.randint(1, 5)
    return f"COUNTER={state['counter']}"


def receiver(sock):
    """Odbiera ACK oraz komendy sterujące od serwera."""
    buffer = ""
    while True:
        try:
            data = sock.recv(1024)
        except OSError:
            break
        if not data:
            print("Serwer zamknął połączenie")
            break
        buffer += data.decode("utf-8", errors="replace")
        while "\n" in buffer:
            line, buffer = buffer.split("\n", 1)
            if line == "ACK":
                continue
            print("Komenda od serwera:", line)
            if line.startswith("SET:SPEED="):
                value = line.split("=", 1)[1]
                if value.isdigit():
                    state["speed"] = int(value)
                    reply = f"ACK:SPEED={value}"
                else:
                    reply = "ERR:INVALID_VALUE"
            else:
                reply = "ERR:UNKNOWN_COMMAND"
            sock.sendall(f"{DEVICE_ID};{reply}\n".encode("utf-8"))


while True:
    try:
        sock = socket.create_connection((SERVER_IP, PORT), timeout=3)
        sock.settimeout(None)
        print(f"{DEVICE_ID}: połączono z {SERVER_IP}:{PORT}")
        threading.Thread(target=receiver, args=(sock,), daemon=True).start()
        while True:
            msg = f"{DEVICE_ID};{measurement()}"
            sock.sendall((msg + "\n").encode("utf-8"))
            print("Wysłano:", msg)
            time.sleep(PERIOD)
    except KeyboardInterrupt:
        print("\nZakończono")
        break
    except OSError as error:
        print("Brak połączenia z serwerem:", error, "- ponowna próba za 3 s")
        time.sleep(3)
