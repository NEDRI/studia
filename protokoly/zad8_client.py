import socket
import time

SERVER_IP = "127.0.0.1"
PORT = 5000
TIMEOUT = 3     j
RETRY_DELAY = 3


def connect():
    """Łączy się z serwerem, ponawiając próby, dopóki się nie uda."""
    while True:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(TIMEOUT)
        try:
            client.connect((SERVER_IP, PORT))
            print("Połączono z serwerem")
            return client
        except socket.timeout:
            print("Serwer nie odpowiada (przekroczono czas połączenia)")
        except ConnectionRefusedError:
            print("Serwer niedostępny (połączenie odrzucone)")
        except OSError as error:
            print("Błąd połączenia:", error)

        client.close()
        print(f"Ponowna próba za {RETRY_DELAY} s (Ctrl+C kończy)")
        time.sleep(RETRY_DELAY)


print("Polecenia: READ:TEMP, READ:SPEED, READ:MOTOR, WRITE:MOTOR:ON/OFF, WRITE:SPEED:<liczba>, exit")

client = None
try:
    client = connect()

    while True:
        message = input("Polecenie: ").strip()

        if not message:
            print("Puste polecenie, wpisz coś")
            continue

        try:
            client.sendall(message.encode("utf-8"))

            if message.lower() == "exit":
                break

            response = client.recv(1024)
            if not response:
                raise ConnectionError("serwer zamknął połączenie")

            print("Odpowiedź serwera:", response.decode("utf-8"))

        except socket.timeout:
            print("Przekroczono czas oczekiwania na odpowiedź")
            client.close()
            client = connect()
        except UnicodeDecodeError:
            print("Nie można odczytać odpowiedzi serwera (błędne kodowanie)")
        except OSError as error:
            print("Błąd komunikacji:", error)
            client.close()
            client = connect()

except (KeyboardInterrupt, EOFError):
    print("\nZakończono")
finally:
    if client:
        client.close()