import socket
import select
import sys


HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

my_username = input("Nazwa użytkownika: ")

cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cli_socket.connect((IP, PORT))

cli_socket.setblocking(False)

username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')

cli_socket.send(username_header + username)

while True:
    sockets_list = [sys.stdin, cli_socket]
    read_sockets, write_socket, error_socket = select.select(
        sockets_list, [], [])

    for socks in read_sockets:
        if socks == cli_socket:
            username_header = cli_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                sys.stdout.write('\u001b[31;1m')
                sys.stdout.write('Połączenie zakończone przez serwer.')
                sys.stdout.write('\u001b[0m\n')
                sys.stdout.flush()
                sys.exit()

            username_length = int(username_header.decode('utf-8').strip())
            username = cli_socket.recv(username_length).decode('utf-8')
            message_header = cli_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = cli_socket.recv(message_length).decode('utf-8')

            print(f"{username} > {message}")
        else:
            message = sys.stdin.readline().rstrip()
            message = message.encode('utf-8')
            message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
            cli_socket.send(message_header + message)