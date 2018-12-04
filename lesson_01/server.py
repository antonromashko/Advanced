import socket
new_list = []


def server_program():
    host = socket.gethostname()
    port = 5000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    conn, address = server_socket.accept()
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        new_list.append(data)
    with open('text.txt', 'w') as f:
        for i in new_list:
            f.write(i + '\n')
    conn.close()


if __name__ == '__main__':
    server_program()