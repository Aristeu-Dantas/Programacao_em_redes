import dpkt
import datetime

arq = "cap1.dump"

#Abrindo o arquivo e denominando as permissões
with open(arq, 'rb') as f:
    pcap = dpkt.pcap.Reader(f)

    #Elaborando as variáveis e construtores
    inicia = None
    termina = None
    maior = 0
    incompletos = 0
    tamanho = 0
    total = 0

    #Determinando o momento de captura
    for timestamp, buf in pcap:
        if inicia is None:
            inicia = datetime.datetime.fromtimestamp(timestamp)
            termina = datetime.datetime.fromtimestamp(timestamp)

        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data

        if len(buf) < ip.len:
            incompletos += 1

        if ip.len > maior:
            maior = ip.len

        tamanho += ip.len
        total += 1

    media = tamanho / total

    print("A captura de pacotes inicia em {0} e termina em {1}."
          "\nO maior pacote capturado é: {2}"
          "\nOs pacotes não salvos são: {3}"
          "\nA média dos tamanhos de pacotes é: {4}"
          .format(inicia,termina,maior,incompletos,media))
