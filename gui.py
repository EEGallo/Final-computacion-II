import tkinter as tk
import asyncio


class ChatGUI:
    def __init__(self, client, loop):
        self.client = client
        self.loop = loop
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.title("ChatConnect - " + self.client.name)
        self.root.geometry('370x680')
        self.root.maxsize(370, 680)
        self.setup_ui()

    def setup_ui(self):
        self.from_message = tk.Frame(
            master=self.root,
            bg="#141414",
            highlightbackground='black',
            highlightcolor='blue',
            highlightthickness=2,
            padx=10,
            pady=10,
        )
        self.scroll_bar = tk.Scrollbar(
            master=self.from_message,
            relief="groove",
            background="#00a8e8"
        )
        self.messages = tk.Listbox(
            master=self.from_message,
            fg="#CED612",
            bg="#26272C",
            yscrollcommand=self.scroll_bar.set
        )
        self.scroll_bar.grid(row=0, column=1, sticky='ns')
        self.messages.grid(row=0, column=0, sticky='nsew')
        self.from_message.grid(row=0, column=0, columnspan=2, sticky='nsew')
        self.from_message.grid_rowconfigure(0, weight=1)
        self.from_message.grid_columnconfigure(0, weight=1)

        self.from_entry = tk.Frame(master=self.root)
        self.text_input = tk.Entry(
            master=self.from_entry,
            font=("Courier-Bold", 14),
            bg="#26272C",
            fg="white",
            relief="flat",
            justify="center",
        )
        self.text_input.grid(row=0, column=0, sticky='ew')
        self.text_input.bind('<Return>', self.on_send)
        self.text_input.insert(0,'')

        self.btn_send = tk.Button(
            master=self.root,
            text='Enviar',
            font=("Courier-Bold", 14),
            bg="black",
            fg="#CED612",
            relief="flat",
            command=self.on_send
        )
        self.from_entry.grid(row=1, column=0, columnspan=2, padx=15, pady=15, sticky='ew')
        self.btn_send.grid(row=1, column=1, padx=10, pady=15, sticky='ew')
        self.from_entry.grid_rowconfigure(0, weight=1)
        self.from_entry.grid_columnconfigure(0, weight=1)

        self.root.configure(background="#141414")
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=0)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=0)

    def on_send(self, event=None):
        message = self.text_input.get()
        if message:
            asyncio.run_coroutine_threadsafe(self.client.send_message(message), self.loop)
            self.messages.insert(tk.END, f'{self.client.name}: {message}')
            self.text_input.delete(0, tk.END)

    def on_close(self):
        self.client.close()
        self.root.destroy()

    def run(self):
        self.root.mainloop()

def start_gui(client, loop):
    gui = ChatGUI(client, loop)
    client.set_messages_widget(gui.messages)
    gui.run()

