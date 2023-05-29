import socket

SERVER_HOST = 'localhost'
SERVER_PORT = 5000

# Cria o socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Digite uma mensagem: ")

    if message:
        # Envia a mensagem para o servidor
        client_socket.sendto(message.encode(), (SERVER_HOST, SERVER_PORT))

    # Recebe as mensagens do servidor e as exibe
    data, _ = client_socket.recvfrom(1024)
    received_message = data.decode()
    print("Mensagem recebida:", received_message)
