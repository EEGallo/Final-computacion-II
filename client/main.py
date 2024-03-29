import socket

def get_input_message():
    return input("Enter your message (or type 'exit' to quit): ")

def send_message(client, username, message):
    try:
        client.send(message.encode('utf-8'))
    except Exception as e:
        print(f"Error sending message: {e}")

if __name__ == '__main__':
    username = input("Enter your username: ")
    print("Type '/msg [username] [message]' to send a private message.")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('localhost', 8080))
        client.send(username.encode('utf-8'))

        while True:
            if client.fileno() == -1:
                print("Connection closed.")
                break
            message_to_send = get_input_message()
            if message_to_send.lower() == 'exit':
                break
            send_message(client, username, message_to_send)

    finally:
        client.close()
