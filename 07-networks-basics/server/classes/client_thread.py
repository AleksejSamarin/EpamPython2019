import logging
from threading import Thread


class ClientThread(Thread):
    threads = []
    logging.basicConfig(format=u'%(asctime)s | %(message)s',
                        datefmt='%Y-%m-%d %I:%M:%S %p',
                        level=logging.DEBUG)

    def __init__(self, address, conn, buffer_size):
        Thread.__init__(self)
        self.ip, self.port = address
        self.conn = conn
        self.buffer_size = buffer_size
        logging.debug(f'[+] {self.ip}:{str(self.port)}')

    def run(self):
        while True:
            try:
                data = self.conn.recv(self.buffer_size)
                logging.debug(f'[M] {self.ip}:{str(self.port)} ({data.decode("utf-8")})')
                for thread in ClientThread.threads:
                    if thread.conn != self.conn:
                        thread.conn.send(f'{self.port}: '.encode("utf-8") + data)
            except ConnectionError:
                logging.debug(f'[-] {self.ip}:{str(self.port)}')
                self.conn.close()
                ClientThread.threads.remove(self)
                break
