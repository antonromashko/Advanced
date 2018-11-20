import socket
import threading


class MultiThreaded:
    def __init__(self, port=5000, host=socket.gethostname(), buffer_size=1024, qty_threads=5):
        self.host = host
        self.port = port
        self.qty_threads = qty_threads
        self.buffer_size = buffer_size
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))

    def listen(self):
        self.server_socket.listen(self.qty_threads)
        while True:
            conn, address = self.server_socket.accept()
            threading.Thread(target=self.listen_client, args=(conn,)).start()

    def listen_client(self, conn):
        while True:
            input_data = conn.recv(self.buffer_size).decode()
            if input_data == '':
                break
            with open('text.txt', 'a') as f:
                f.write(input_data + '\n')
        conn.close()


d = MultiThreaded()
d.listen()
