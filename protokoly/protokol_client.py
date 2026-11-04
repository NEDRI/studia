import socket

SERVER_IP = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

print("Połączono z serwerem")
print("Polecenia: READ:TEMP, READ:SPEED, READ:MOTOR, WRITE:MOTOR:ON, WRITE:MOTOR:OFF, exit")

while True:
    message = input("Polecenie: ")
    client.sendall(message.encode("utf-8"))

    if message.lower() == "exit":
        break

    response = client.recv(1024)
    print("Odpowiedź serwera:", response.decode("utf-8"))

client.close()