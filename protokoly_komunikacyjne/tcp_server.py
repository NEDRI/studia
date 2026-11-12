import socket

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Serwer TCP nasłuchuje na {HOST}:{PORT}")
conn, addr = server.accept()
print("Połączono z:", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break

    message = data.decode("utf-8")
    print("Odebrano:", message)

    if message.lower() == "exit":
        break

    conn.sendall(f"ACK: {message}".encode("utf-8"))

conn.close()
server.close()