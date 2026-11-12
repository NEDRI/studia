# Lab2, Zadanie 7 – komunikacja dwukierunkowa (klient TCP)
import socket

SERVER_IP = "127.0.0.1"   # dla komunikacji między stanowiskami: IP sąsiada
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))
print("Połączono z serwerem")
print("Polecenia: READ:TEMP | READ:SPEED | READ:MOTOR | READ:ALARM | READ:STATUS")
print("           WRITE:MOTOR:ON | WRITE:MOTOR:OFF | WRITE:SPEED:<n> | RESET:ALARM | exit")

while True:
    message = input("Klient -> ").strip()
    if not message:
        continue
    client.sendall(message.encode("utf-8"))
    if message.lower() == "exit":
        break
    response = client.recv(1024).decode("utf-8")
    print("Serwer ->", response)

    # Klient reaguje na treść odpowiedzi
    if "ALARM=1" in response:
        print("  !!! Urządzenie zgłasza ALARM – wyślij RESET:ALARM po usunięciu przyczyny")
    elif response.startswith("ERR"):
        print("  Serwer odrzucił polecenie")

client.close()
