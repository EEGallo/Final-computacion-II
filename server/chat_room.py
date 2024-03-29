from datetime import datetime


class ChatRoom:
    def __init__(self):
        self.users = {}
        print("Users in the chat room:", [user.username for user in self.users.values()])

    def add_user(self, user):
        self.users[user.username] = user

    def remove_user(self, user):
        del self.users[user.username]

    def broadcast_message(self, sender, message):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        


        parts = message.split(' ', 2)
        if len(parts) >= 3 and parts[0].lower() == '/msg':
            recipient_username = parts[1]
            private_message = parts[2]
            recipient = self.users.get(recipient_username)
            try:
                if recipient:
                    private_msg = f"(Private) {current_time} {sender.username}: {private_message}"
                    print(f"Sending private message to {recipient.username}: {private_msg}")
                    recipient.send_message(private_msg)
                    sender.send_message(f"(Private to {recipient.username}): {private_message}")
                else:
                    sender.send_message(f"User {recipient_username} not found.")

            except Exception as e:
                print(f"Error sending private message: {e}")
        else:
            public_msg = f"{current_time} {sender.username}: {message}"
            for user in self.users.values():
                try:
                    user.send_message(public_msg)
                except Exception as e:
                    print(f"Error broadcasting message: {e}")