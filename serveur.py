
import sys
import socket, threading
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

# AES
KEY = b'0123456789abcdef'  # 16 bytes
CIPHER = AES.new(KEY, AES.MODE_ECB)

#### SERVER ####
SERVER : str = "127.0.0.1"
PORT : int = 7500
ADDRESS : tuple = (SERVER, PORT)
FORMAT : str = "utf-8"
HEADER : int = 1024
LISTEN_LIMIT : int = 5

active_connections : int = 0
clients, names = [], []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server.bind(ADDRESS)
except socket.error as e:
    print(str(e))
    print(f"Unable to bind to host {SERVER} and port {PORT}!")


def log_message(message) -> None:
    print(message)
    with open("server_msg_enc_dec.txt", "a") as file:
        file.write(message + "\n")


def startChat() -> None:
    global active_connections
    log_message("server is working on " + SERVER)
    server.listen(LISTEN_LIMIT)
    while True:
        conn, addr = server.accept()
        conn.send("NAME".encode(FORMAT))
        name : str = conn.recv(HEADER).decode(FORMAT)
        names.append(name)
        clients.append(conn)
        active_connections += 1
        log_message(f"\nName is : {name}")

        send_message_to_client(f"{name} has joined the chat! ".encode(FORMAT))

        thread = threading.Thread(target=handle, args=(conn, addr, ))
        thread.start()

        log_message(f"Active connections: {active_connections}")
        check_active_connections()


def handle(conn, addr) -> None:
    global active_connections
    log_message(f"new connection {addr}")
    disconnected : bool = False
    while True:
        try:
            encoded_msg = conn.recv(HEADER).decode(FORMAT)
            ciphertext = b64decode(encoded_msg.encode('utf-8'))
            decrypted_msg = CIPHER.decrypt(ciphertext).strip().decode('latin1')

            log_message(f"[ENCRYPTED] {addr} > {encoded_msg}")
            log_message(f"[DECRYPTED] {addr} > {decrypted_msg}")

            # For all clients, send the decrypted message
            send_message_to_client(decrypted_msg.encode(FORMAT))
        except:
            disconnected = True
            break

    index : int = clients.index(conn)
    clients.remove(conn)
    conn.close()
    name : str = names[index]
    send_message_to_client(f"{name} has left the chat!".encode(FORMAT))
    names.remove(name)
    active_connections -= 1
    check_active_connections()

    if disconnected:
        log_message(f"\nClient {addr} has disconnected!")
        log_message(f"Active connections {active_connections}")


def send_message_to_client(message) -> None:
    for client in clients:
        client.send(message)


def check_active_connections() -> None:
    global active_connections
    if active_connections == 0:
        log_message("ALL clients are disconnected!")
        server.close()
        sys.exit()


def main(args) -> None:
    log_message("Server is starting...")
    log_message(f"active connections {threading.active_count()-1}")
    startChat()
    log_message("Server is closed!...")


if __name__ == "__main__":
    main(sys.argv)





