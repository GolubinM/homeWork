import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 4321

client_socket.connect((host, port))

server_message = client_socket.recv(1024).decode()
print(server_message)

while True:
    client_message = input('Введите сообщение: ')
    client_socket.send(client_message.encode())

    if client_message == "":
        print('Отключаемся от сервера...')
        break

    server_response = client_socket.recv(2048).decode()
    print(f'Ответ сервера:\n{server_response}')

client_socket.close()
