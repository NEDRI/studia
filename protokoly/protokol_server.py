import socket

HOST = "127.0.0.1"
PORT = 5000

temperature = 23.7
speed = 1450
motor = "OFF"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
    print("Odebrano:", command)

    if command == "EXIT":
        break

    if command == "READ:TEMP":
        response = f"TEMP={temperature}"
    elif command == "READ:SPEED":
        response = f"SPEED={speed}"
    elif command == "READ:MOTOR":
        response = f"MOTOR={motor}"
    elif command == "WRITE:MOTOR:ON":
        motor = "ON"
        response = "ACK"
    elif command == "WRITE:MOTOR:OFF":
        motor = "OFF"
        response = "ACK"
    else:
        response = "ERR:UNKNOWN_COMMAND"

    print("Wysłano:", response)
    conn.sendall(response.encode("utf-8"))

conn.close()
server.close()