import time,hashlib

def findNoncestriong (dataToHash,bitsToBeZero):
    Inicio = time.time()

    max_nonce = (2**32) + 1
    for nonce in range (max_nonce) :
        h = hashlib.sha256()
        h.update(nonce.to_bytes(4,"big") + (dataToHash))
        hash = h.digest()
        n = int.from_bytes(hash[:4],"big")

        if n >> (32 - bitsToBeZero) == 0:
            print(f"Nonce: {nonce:032b}; Hash: {n:032b}") # TESTES
            break

    Final = time.time()
    tempo = Final - Inicio
    return nonce, tempo 

'''
a = "Giovanna Camila" #um conjunto de bytes
a = bytes(a, "utf-8")
b = 15 # o número de bits iniciais que deve ser zero no hash.
valores = [findNoncestriong(a,b)]

#print(findNoncestriong(f"Nonce: {a}; Tempo de execução:{b}s"))

print((f"Nonce: {valores[0][0]}; Tempo de execução: {valores[0][1]}s"))
'''