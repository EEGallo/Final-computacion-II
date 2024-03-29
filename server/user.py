class User:
    def __init__(self, username, socket):
        self.username = username
        self.socket = socket

    def send_message(self, message):
        self.socket.send(message.encode('utf-8'))
