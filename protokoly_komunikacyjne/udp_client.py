import socket

SERVER_IP = "127.0.0.1"
PORT = 5001

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(3)

while True:
    message = input("Wpisz wiadomość: ")
    client.sendto(message.encode("utf-8"), (SERVER_IP, PORT))

    if message.lower() == "exit":
        break

    try:
        data, address = client.recvfrom(1024)
        print("Odpowiedź serwera:", data.decode("utf-8"))
    except socket.timeout:
        print("Brak odpowiedzi serwera.")

client.close()