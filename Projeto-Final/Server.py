import socket, threading, sys

# Lista para armazenar todas as conexões de clientes ativos
client_connections = []
client_addresses = []

def handle_client(client_socket, address):
    while True:
        try:
            data = client_socket.recv(4096).decode('utf-8')
            if not data:
                remove_client(client_socket)
                break

            # Processar os comandos recebidos do cliente
            process_command(data, client_socket, address)

        except Exception as e:
            print(f"Erro na conexão com {address}: {e}")
            remove_client(client_socket)
            break

def process_command(command, client_socket, address):
    # Separa o comando e os argumentos utilizando espaço como delimitador
    command_parts = command.split(" ")
    cmd = command_parts[0]

    if cmd == "/q":
        # Comando /q → sair do cliente;
        remove_client(client_socket)
    elif cmd == "/u":
        # Comando /u → listar o IP:porta dos clientes conectados no servidor;
        list_connected_clients()
    elif cmd.startswith("/m:"):
        # Comando /m:ip_destino:porta:mensagem → Enviar uma mensagem a um determinado cliente conectado no servidor
        send_private_message(cmd[3:], client_socket)
    elif cmd == "/b":
        # Comando /b:mensagem → Enviar uma mensagem para todos os clientes conectados no servidor
        broadcast_message(command[3:], client_socket)
    elif cmd == "/h":
        # Comando /h → listar as mensagens já enviadas ao servidor pelo usuário (histórico);
        list_user_history(client_socket)
    elif cmd == "/f":
        # Comando /f → listar os arquivos (nome e tamanho) contidos na pasta /server_files (do servidor);
        list_server_files(client_socket)
    elif cmd.startswith("/d:"):
        # Comando /d:nome_arquivo → efetuar o “download” do arquivo especificado para a pasta /download (do cliente);
        download_file(command[3:], client_socket)
    elif cmd.startswith("/u:"):
        # Comando /u:nome_arquivo → efetuar o “upload” de um arquivo para a pasta /server_files (do servidor);
        upload_file(command[3:], client_socket)
    elif cmd.startswith("/w:"):
        # Comando /w:url → efetuar o download do arquivo fornecido na url para a pasta /server_files (do servidor);
        download_file_from_url(command[3:], client_socket)
    elif cmd.startswith("/rss:"):
        # Comando /rss:palavra_chave → listar as 10 notícias mais recentes que contenham a palavra_chave
        rss_keyword_search(command[5:], client_socket)
    elif cmd == "/?":
        # Comando /? → exibir uma ajuda (listar as opções contidas nesse roteiro).
        show_help(client_socket)
    else:
        # Comando inválido
        client_socket.send("Comando inválido. Digite /? para ver a lista de comandos disponíveis.".encode('utf-8'))


def remove_client(client_socket):
    if client_socket in client_connections:
        index = client_connections.index(client_socket)
        client_connections.remove(client_socket)
        client_socket.close()
        address = client_addresses[index]
        client_addresses.remove(address)
        print(f"Cliente {address} desconectado.")

def start_server():
    server_ip = '127.0.0.1'
    server_port = 5000

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, server_port))
    server.listen(5)
    print("Servidor iniciado. Aguardando conexões...")

    while True:
        try:
            client_socket, client_address = server.accept()
            client_connections.append(client_socket)
            client_addresses.append(client_address)
            print(f"Cliente {client_address} conectado.")

            client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_handler.start()
        except Exception as e:
            print(f"Erro ao aceitar conexão: {e}")
            break

    server.close()

if __name__ == "__main__":
    start_server()
