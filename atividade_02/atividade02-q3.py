import hashlib
import time

#função para encontrar os zeros do hash
def main(zeros_alvo, texto):
    prefixo = bytes(texto, 'utf-8')
    for i in range(2**32):
        sufixo = i.to_bytes(4, 'big')
        hash_sha1 = hashlib.sha1(prefixo + sufixo).digest()
        if hash_sha1[:zeros_alvo] == bytes(zeros_alvo):
            return sufixo
    return

#função para contar o tempo utilizado
def medir_tempo(zeros_alvo, texto):
    tempo_inicial = time.time()
    sufixo = main(zeros_alvo, texto)
    tempo_final = time.time()
    tempo_utilizado = tempo_final - tempo_inicial
    return tempo_utilizado, sufixo

#recebe string
texto = input("Digite uma string: ")
zeros_alvo = 5

tempo, sufixo = medir_tempo(zeros_alvo, texto)

print(f"String: {texto}.",f"\nTempo: {tempo} segundos.", f"\n4 bytes encontrados: {sufixo}")

if __name__ == '__main__':
    main()
