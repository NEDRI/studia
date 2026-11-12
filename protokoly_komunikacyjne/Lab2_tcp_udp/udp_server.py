import socket
HOST = "127.0.0.1"
PORT = 5001
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))
print(f"Serwer UDP działa na {HOST}:{PORT}")
print("Oczekiwanie na wiadomości...")
while True:
 data, address = server.recvfrom(1024)
 message = data.decode("utf-8")
 print(f"Odebrano od {address}: {message}")
 if message.lower() == "exit":
    break
 response = f"ACK: {message}"
 server.sendto(response.encode("utf-8"), address)
server.close()
