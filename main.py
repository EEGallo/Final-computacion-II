from client import Client
import tkinter as tk
import argparse


def main(host, port):
    #inicializar y ejecutar la aplicación GUI

    client = Client(host, port)
    receive = client.start()
    window = tk.Tk()
    window.title("ChatConnect - " + receive.name)
    window.geometry('370x680')
    window.maxsize(370, 680)

    fromMessage = tk.Frame(
        master=window,
        bg="#141414",
        highlightbackground='black',
        highlightcolor='blue', 
        highlightthickness=2,
        padx=10, 
        pady=10,
        )
    
    scrollBar = tk.Scrollbar(
        master=fromMessage,
        relief="groove",
        background="#00a8e8"
        )
    
    messages = tk.Listbox(
        master=fromMessage,
        fg="#CED612",
        bg="#26272C",
        yscrollcommand=scrollBar.set
        )
    
    scrollBar.grid(row=0, column=1, sticky='ns')
    messages.grid(row=0, column=0, sticky='nsew')
    fromMessage.grid(row=0, column=0, columnspan=2, sticky='nsew')
    
    fromMessage.grid_rowconfigure(0, weight=1)
    fromMessage.grid_columnconfigure(0, weight=1)
    
    client.messages = messages
    receive.messages = messages

    fromEntry = tk.Frame(master=window)
    textInput = tk.Entry(
        master=fromEntry,
        font=("Courier-Bold",14),
        bg="#26272C",
        fg="white",
        relief="flat",
        justify="center",
        )

    textInput.grid(row=0, column=0, sticky='ew')
    textInput.bind('<Return>', lambda x:client.send(textInput))
    textInput.insert(0, 'Escriba aquí su mensaje.')

    btnSend = tk.Button(
        master=window,
        text='Enviar',
        font=("Courier-Bold",14),
        bg="black",
        fg="#CED612",
        relief="flat",
        command=lambda:client.send(textInput)
        )
    
    fromEntry.grid(row=1, column=0, columnspan=2, padx=15, pady=15, sticky='ew')
    btnSend.grid(row=1, column=1, padx=10, pady=15, sticky='ew')
    
    fromEntry.grid_rowconfigure(0, weight=1)
    fromEntry.grid_columnconfigure(0, weight=1)

    window.configure(background="#141414")

    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=0)
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=0)

    window.mainloop()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ChatConnect Server')
    parser.add_argument('host', help='Interfaz en la que escucha el servidor')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060, help='TCP port(default 1060)')

    args = parser.parse_args()

    main(args.host, args.p)