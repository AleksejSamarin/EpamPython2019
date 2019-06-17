import configparser
import logging
import os
import socket
import sys
from threading import Thread


def listen_income():
    while True:
        try:
            data = client_socket.recv(int(config['buffer']['size']))
            print('User #' + data.decode('utf-8'))
        except ConnectionError:  # exit message
            exit_program()


def send_messages():
    while True:
        message = input('')
        if message == 'exit':
            exit_program()
        try:
            client_socket.send(message.encode('utf-8'))
        except OSError:
            logging.error('Server is closed')
            exit_program()


def exit_program():
    client_socket.close()
    sys.exit()


if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))
    config = configparser.ConfigParser()
    config.read(os.path.join(path, './configs/client.ini'))
    logging.basicConfig(format=u'Error has been occurred. %(message)s (%(asctime)s)',
                        datefmt='%Y-%m-%d %I:%M:%S %p',
                        level=logging.ERROR)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((config['server']['ip'], int(config['server']['port'])))
    except ConnectionRefusedError:
        logging.error('Cannot connect to server')
        exit_program()

    threads = []
    thread_tasks = (listen_income, send_messages)
    for task in thread_tasks:
        thread = Thread(target=task)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    exit_program()
