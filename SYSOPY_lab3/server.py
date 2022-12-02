import socket
import select


HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

srv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

srv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

srv_socket.bind((IP, PORT))

srv_socket.listen()

sockets_list = [srv_socket]

clients = {}

print(f'Nasłuchiwanie {IP}:{PORT}...')


def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header):
            return False
        message_length = int(message_header.decode('utf-8').strip())
        return {'header': message_header, 'data': client_socket.recv(message_length)}
    except:
        return False


while True:
    read_sockets, _, exception_sockets = select.select(
        sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == srv_socket:
            client_socket, client_address = srv_socket.accept()
            user = receive_message(client_socket)
            if user is False:
                continue
            sockets_list.append(client_socket)
            clients[client_socket] = user
            print('Zaakceptowano nowe połączenie z {}:{}, nazwa użytkownika: {}'.format(
                *client_address, user['data'].decode('utf-8')))
        else:
            message = receive_message(notified_socket)
            if message is False:
                print('Zakończono połączenie z: {}'.format(
                    clients[notified_socket]['data'].decode('utf-8')))
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            user = clients[notified_socket]
            print(
                f'Odebrano wiadomość od {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(
                        user['header'] + user['data'] + message['header'] + message['data'])
