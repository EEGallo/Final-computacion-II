import asyncio


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.name = None
        self.reader = None
        self.writer = None
        self.messages_widget = None

    async def connect(self):
        self.reader, self.writer = await asyncio.open_connection(self.host, self.port)
        print(f'Conectado con éxito a {self.host}:{self.port}')
        self.name = input('Tu Nombre: ')
        print(f'Bienvenido, {self.name}! Prepararse para enviar y recibir mensajes...')
        self.writer.write(f'Servidor: {self.name} se ha unido al chat!'.encode('ascii'))
        await self.writer.drain()

    async def send_message(self, message):
        self.writer.write(f'{self.name}: {message}'.encode('ascii'))
        await self.writer.drain()

    async def receive_messages(self):
        while True:
            data = await self.reader.read(100)
            message = data.decode()
            if message:
                if self.messages_widget:
                    self.messages_widget.insert('end', message)
                    print(f'\r{message}\n{self.name}: ', end='')
                else:
                    print(f'\r{message}\n{self.name}: ', end='')
            else:
                print('\n¡Hemos perdido la conexión con el servidor!')
                print('\nAbandonando sala...')
                break

    def set_messages_widget(self, widget):
        self.messages_widget = widget

    def close(self):
        if self.writer:
            self.writer.close()
            asyncio.run(self.writer.wait_closed())
