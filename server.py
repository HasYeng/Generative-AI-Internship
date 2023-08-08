import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

serv_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_s.bind((HOST, PORT))
serv_s.listen()
clients = {}


def broadcast(message, sender=None):
    """
    Broadcasts a message to all connected clients except the sender.
    """

    for client in clients:
        if clients[client]:
            if client != sender:
                client.send(message.encode())


def handle_client(client_s, address):
    """
    Handles a connected client's communication in a dedicated thread.
    """

    try:
        client_s.send("Hello! Type 'quit' to quit.".encode())
        nickname = client_s.recv(1024).decode()
        clients[client_s] = nickname
        broadcast(f"{nickname} joined the chat!", client_s)

        while True:
            message = client_s.recv(1024).decode()
            if not message or message.lower() == 'quit':
                break
            broadcast(f"{message}", sender=client_s)
            print(f"Received from {message}")

        print(f"{clients[client_s]} left the chat.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        del clients[client_s]
        client_s.close()


while True:
    client_socket, address = serv_s.accept()
    clients[client_socket] = None

    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()
