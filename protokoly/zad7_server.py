# Lab2, Zadanie 7 – komunikacja dwukierunkowa (serwer TCP)
import socket

HOST = "127.0.0.1"   # dla komunikacji między stanowiskami: "0.0.0.0"
PORT = 5000

temperature = 23.7
speed = 1450
motor = "OFF"
alarm = 0
SPEED_LIMIT = 3000   # powyżej tej prędkości zgłaszany jest alarm


def update_process():
    """Prosta symulacja procesu: pracujący silnik grzeje urządzenie."""
    global temperature, alarm
    if motor == "ON":
        temperature = round(temperature + 0.4, 1)
    elif temperature > 20:
        temperature = round(temperature - 0.2, 1)
    if speed > SPEED_LIMIT or temperature > 80:
        alarm = 1


def handle_command(command):
    global motor, speed, alarm

    if command == "READ:TEMP":
        return f"TEMP={temperature}"
    if command == "READ:SPEED":
        return f"SPEED={speed}"
    if command == "READ:MOTOR":
        return f"MOTOR={motor}"
    if command == "READ:ALARM":
        return f"ALARM={alarm}"
    if command == "READ:STATUS":
        return f"MOTOR={motor};SPEED={speed};TEMP={temperature};ALARM={alarm}"
    if command in ("WRITE:MOTOR:ON", "WRITE:MOTOR:OFF"):
        if command.endswith("ON") and alarm:
            return "ERR:ALARM_ACTIVE"
        motor = command.split(":")[2]
        return f"ACK:MOTOR={motor}"
    if command.startswith("WRITE:SPEED:"):
        value = command.split(":")[2]
        if not value.isdigit():
            return "ERR:INVALID_VALUE"
        speed = int(value)
        return f"ACK:SPEED={speed}"
    if command == "RESET:ALARM":
        alarm = 0
        return "ACK:ALARM=0"
    return "ERR:UNKNOWN_COMMAND"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)
print(f"Serwer automatyki nasłuchuje na {HOST}:{PORT}")

conn, addr = server.accept()
print("Połączono z:", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    command = data.decode("utf-8").strip().upper()
    print("Klient ->", command)
    if command == "EXIT":
        break
    update_process()
    response = handle_command(command)
    print("Serwer ->", response)
    conn.sendall(response.encode("utf-8"))

conn.close()
server.close()
