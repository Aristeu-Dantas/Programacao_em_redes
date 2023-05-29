import os

def cifra_xor(arquivo, palavra_chave):
    with open(arquivo, 'rb') as f:
        conteudo_original = bytearray(f.read())

    chave = [ord(c) for c in palavra_chave]

    conteudo_cifrado = bytearray(b ^ chave[i % len(chave)] for i, b in enumerate(conteudo_original))

    novo_arquivo = arquivo + '.enc'
    with open(novo_arquivo, 'wb') as f:
        f.write(conteudo_cifrado)

    os.remove(arquivo)

    print(f'Arquivo cifrado gerado: {novo_arquivo}')

arquivo = input('Digite o nome do arquivo: ')
palavra_chave = input('Digite a palavra-chave: ')

cifra_xor(arquivo, palavra_chave)
