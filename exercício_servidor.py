import socket

# Escuta em todas as interfaces locais
SERVER_HOST = ''
SERVER_PORT = 5000
MAX_MESSAGE_SIZE = 64

# Dicionário para armazenar os endereços dos clientes
clients = {}

# Cria o socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))

print('Servidor de Chat UDP iniciado no {}:{}'.format(SERVER_HOST, SERVER_PORT))

while True:
    data, client_address = server_socket.recvfrom(MAX_MESSAGE_SIZE)
    message = data.decode()

    if not message:
        continue

    if client_address not in clients:
        clients[client_address] = True

    # Replicar a mensagem para todos os clientes (exceto o remetente)
    for client in clients:
        if client != client_address:
            server_socket.sendto(data, client)
