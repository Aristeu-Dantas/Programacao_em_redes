# if __name__ == '__main__':
#     server_ip = input("Digite o endereço IP do servidor (ou pressione Enter para usar todas as interfaces locais): ")
#     if not server_ip:
#         server_ip = '0.0.0.0'
#     start_server(server_ip)

import socket

SERVER_IP= "10.27.2.242"
SERVER_PORT=54321
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind('',SERVER_PORT)

hostInfo= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for ip in hostInfo[2]:
    print(f'Escutando em {ip}:{SERVER_PORT}')

clients=set()

while True:
    message = input("Mensagem: ").encode("utf-8")
    if message != "":
        sock.sendto(message.encode("utf-8"),(SERVER_IP,SERVER_PORT))


    data, src = sock.recvfrom(64)
    print(data.decode("uft-8"))
sock.close()
