import threading
import socket
import sys
import os
import tkinter as tk



class Send(threading.Thread):

    #Escucha la entrada del usuario desde la línea de comandos

    # sock: El socket de conexión
    #name (str) : El nombre de usuario proporcionado por el usuario

    def __init__(self, sock, name):
        super().__init__()
        self.sock = sock
        self.name = name
    
    def run(self):
        
        #Escuchar la entrada del usuario desde la línea de comandos y enviarla al servidor

        while True:
            print('{}: '.format(self.name), end='')
            sys.stdout.flush()
            message = sys.stdin.readline()[:-1]

        #Si escribe 'quit' se cerrará la conexión y saldrás de la app.
        
            if message == 'quit':
                self.sock.sendall('Server: {} has left the chat.'.format(self.name).encode('ascii'))
                break
            
            else:
                self.sock.sendall('{}: {}'.format(self.name, message).encode('ascii'))
        
        print('\nAbandonando sala...')
        self.sock.close()
        os.exit(0)
    

class Receive(threading.Thread):

    #Escuchar los mensajes entrantes del servidor
    def __init__(self, sock, name):

        super().__init__()
        self.sock = sock
        self.name = name
        self.messages = None

    def run(self):

        #Recibe datos del servidor y los muestra en la GUI (interfaz gráfica de usuario)

        while True:
            message = self.sock.recv(1024).decode('ascii')

            if message:
                if self.messages:
                    self.messages.insert(tk.END, message)
                    print('\r{}\n{}: '.format(message, self.name), end = '')

                else:
                    print('\r{}\n{}: '.format(message, self.name), end = '')

            else:
                print('\n ¡Hemos perdido la conexión con el servidor!')
                print('\nAbandonando sala...')
                self.sock.close()
                sys.exit(0)


class Client:

    #Gestión de la conexión cliente-servidor e integración de GUI

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.name = None
        self.messages = None

    def start(self):
        print('Intentando conectar con {}:{}...'. format(self.host, self.port))

        self.sock.connect((self.host, self.port))
        print('Conectado con éxito a {}:{}'.format(self.host, self.port))

        print()

        self.name = input('Tu Nombre: ')
        print()

        print('Bienvenido, {}! Prepararse para enviar y recibir mensajes...'.format(self.name))

        # Crear threads de envío y recepción

        send = Send(self.sock, self.name)
        receive = Receive(self.sock, self.name)

        # iniciar el thread de envío y recepción
        send.start()
        receive.start()

        self.sock.sendall('Servidor: {} se ha unido al chat!'.format(self.name).encode('ascii'))
        print('\r¡Listo! Abandona la sala de chat en cualquier momento escribiendo "quit".\n')
        print('{}: '.format(self.name), end='')

        return receive
            

    def send(self, textInput):
        
        #Envía datos textInput desde la GUI

        message = textInput.get()
        textInput.delete(0, tk.END)
        self.messages.insert(tk.END, '{}:{}'.format(self.name, message))

        # Escribir "QUIT" para salir de la sala

        if message == "quit":
            self.sock.sendall('Servidor: {} ha abandonado el chat.'.format(self.name).encode('ascii'))

            print('\nAbandonando...')
            self.sock.close()
            sys.exit(0)

        # ENVIAR mensaje al servidor para su difusión
        else:
            self.sock.sendall('{}:{}'.format(self.name, message).encode('ascii'))