import socket
import multiprocessing
from user import User
from chat_room import ChatRoom

def handle_client(client_socket, chat_room):
    username = client_socket.recv(1024).decode('utf-8')
    user = User(username, client_socket)
    chat_room.add_user(user)

    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"{username}: {message}")
            chat_room.broadcast_message(user, message)
    except Exception as e:
        print(f"Error handling client {username}: {e}")

    chat_room.remove_user(user)
    client_socket.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 8080))
    server.listen(5)
    print("Server listening on port 8080...")

    chat_room = ChatRoom()  # Mover la creación de la sala de chat aquí

    while True:
        client, addr = server.accept()
        print(f"Accepted connection from {addr[0]}:{addr[1]}")
        client_handler = multiprocessing.Process(target=handle_client, args=(client, chat_room))
        client_handler.start()

if __name__ == '__main__':
    start_server()