import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

client_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def receive_messages():
    """
    Receives messages from the server and prints them to the console.
    """
    while True:
        message = client_s.recv(1024).decode()
        if message:
            print(message)


try:
    client_s.connect((HOST, PORT))
    welcome_m = client_s.recv(1024).decode()
    print(welcome_m)

    message_thread = threading.Thread(target=receive_messages)
    message_thread.start()

    username = input("Enter your username: ")
    client_s.send(username.encode())

    while True:
        message = input()
        if message.lower() == 'quit':
            client_s.send(message.encode())
            break
        client_s.send(f"{username}: {message}".encode())

except Exception as e:
    print(f"Error: {e}")
finally:
    client_s.close()
