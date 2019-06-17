import configparser
import os
import socket
from classes import ClientThread


def event_loop():
    while True:
        conn, address = server_socket.accept()
        new_thread = ClientThread(address, conn, int(config['buffer']['size']))
        new_thread.start()
        ClientThread.threads.append(new_thread)


if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))
    config = configparser.ConfigParser()
    config.read(os.path.join(path, './configs/server.ini'))
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((config['address']['ip'], int(config['address']['port'])))
    server_socket.listen(1)
    try:
        event_loop()
    finally:
        for thread in ClientThread.threads:
            thread.join()
        server_socket.close()
