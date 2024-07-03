import asyncio
import argparse
from threading import Thread
from gui import start_gui


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
        try:
            while True:
                data = await self.reader.read(100)
                message = data.decode()
                if message:
                    if self.messages_widget:
                        self.messages_widget.after(0, lambda: self.messages_widget.insert('end', message))
                        self.messages_widget.after(0, lambda: print(f'\r{message}\n{self.name}: ', end=''))
                    else:
                        print(f'\r{message}\n{self.name}: ', end='')
                else:
                    print('\n¡Hemos perdido la conexión con el servidor!')
                    print('\nAbandonando sala...')
                    break
        except Exception as e:
            print(f'Error al recibir mensajes: {e}')

    def set_messages_widget(self, widget):
        self.messages_widget = widget

    def close(self):
        if self.writer:
            self.writer.close()
            asyncio.run(self.writer.wait_closed())
            

async def main(host, port):
    client = Client(host, port)
    await client.connect()

    loop = asyncio.get_running_loop()
    gui_thread = Thread(target=start_gui, args=(client, loop))
    gui_thread.start()

    await client.receive_messages()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ChatConnect Client')
    parser.add_argument('host', help='Interfaz en la que se conecta el cliente')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060, help='TCP port (default 1060)')

    args = parser.parse_args()
    asyncio.run(main(args.host, args.p))