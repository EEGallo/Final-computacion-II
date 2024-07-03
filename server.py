import asyncio
import argparse

class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = []

    async def handle_client(self, reader, writer):
        addr = writer.get_extra_info('peername')
        self.clients.append(writer)
        print(f'{addr} está conectado')

        try:
            while True:
                data = await reader.read(100)
                if not data:
                    break
                message = data.decode()
                print(f'{message}')
                
                self.broadcast(message, writer)
                
        except ConnectionResetError:
            print(f'La conexión con {addr} se ha cerrado inesperadamente')
        except Exception as e:
            print(f'Se ha producido un error con {addr}: {e}')
        finally:
            if writer in self.clients:
                self.clients.remove(writer)
            writer.close()
            await writer.wait_closed()
            print(f'{addr} se ha desconectado')


    def broadcast(self, message, sender_writer):
        for client in self.clients:
            if client != sender_writer:
                try:
                    client.write(message.encode())
                    asyncio.create_task(client.drain())
                except ConnectionResetError:
                    print(f'Error al enviar mensaje a un cliente desconectado')
                except Exception as e:
                    print(f'Error desconocido al enviar mensaje: {e}')

    async def run(self):
        server = await asyncio.start_server(self.handle_client, self.host, self.port)
        print(f"Iniciando servidor en el host: {self.host} port:{self.port}")

        async with server:
            await server.serve_forever()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Servidor de Chat')
    parser.add_argument('host', help='Interfaz en la que se conecta el servidor')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060, help='Puerto TCP (por defecto 1060)')

    args = parser.parse_args()
    server = ChatServer(args.host, args.p)
    asyncio.run(server.run())
