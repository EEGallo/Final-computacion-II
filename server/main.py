import multiprocessing
from chat_server import start_server

if __name__ == '__main__':
    # Start the server process
    server_process = multiprocessing.Process(target=start_server)
    server_process.start()
    server_process.join()