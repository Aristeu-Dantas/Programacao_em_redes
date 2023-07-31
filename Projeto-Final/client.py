import socket

def send_message(server_ip, server_port, message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    client_socket.send(message.encode('utf-8'))
    response = client_socket.recv(4096).decode('utf-8')
    print(response)
    client_socket.close()

if __name__ == "__main__":
    server_ip = '127.0.0.1'
    server_port = 5000

    while True:
        message = input("Digite um comando (/q para sair): ")
        if message == '/q':
            print("Encerrando o cliente.")
            break
        send_message(server_ip, server_port, message)
