import socket

HOST = "127.0.0.1"
PORT = 5000

temperature = 23.7
speed = 1450
motor = "OFF"


def handle_command(command):
    """Interpretuje polecenie i zwraca odpowiedź protokołu."""
    global motor, speed

    parts = command.split(":")

    if parts[0] == "READ":
        if len(parts) != 2:
            return "ERR:BAD_FORMAT"
        if parts[1] == "TEMP":
            return f"TEMP={temperature}"
        if parts[1] == "SPEED":
            return f"SPEED={speed}"
        if parts[1] == "MOTOR":
            return f"MOTOR={motor}"
        return "ERR:UNKNOWN_PARAMETER"

    if parts[0] == "WRITE":
        if len(parts) > 3:
            return "ERR:BAD_FORMAT"
        if len(parts) < 3 or parts[2] == "":
            return "ERR:MISSING_VALUE"
        name, value = parts[1], parts[2]

        if name == "MOTOR":
            if value not in ("ON", "OFF"):
                return "ERR:INVALID_VALUE"
            motor = value
            return "ACK"

        if name == "SPEED":
            try:
                speed = int(value)
            except ValueError:
                return "ERR:INVALID_VALUE" 
            return "ACK"

        return "ERR:UNKNOWN_PARAMETER"

    return "ERR:UNKNOWN_COMMAND"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)

print(f"Serwer automatyki nasłuchuje na {HOST}:{PORT}")

try:
    while True:
        conn, addr = server.accept()
        print("Połączono z:", addr)

        try:
            while True:
                data = conn.recv(1024)
                if not data:
                    print("Klient zamknął połączenie")
                    break

                try:
                    command = data.decode("utf-8").strip().upper()
                except UnicodeDecodeError:
                    print("Nie można zdekodować danych:", data)
                    conn.sendall(b"ERR:DECODE")
                    continue

                print("Odebrano:", command)

                if command == "EXIT":
                    print("Klient zakończył sesję")
                    break

                response = handle_command(command)
                print("Wysłano:", response)
                conn.sendall(response.encode("utf-8"))

        except ConnectionResetError:
            print("Połączenie zostało zerwane przez klienta")
        except OSError as error:
            print("Błąd komunikacji:", error)
        finally:
            conn.close()
            print("Czekam na kolejnego klienta...")

except KeyboardInterrupt:
    print("\nZatrzymano serwer")
finally:
    server.close()