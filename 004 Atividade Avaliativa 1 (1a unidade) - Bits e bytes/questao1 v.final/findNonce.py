import time,hashlib

def findNonce (dataToHash,bitsToBeZero):
    Inicio = time.time() # Calcular tempo de execução


    #######
    max_nonce = (2**32) + 1
    for nonce in range (max_nonce) :
        h = hashlib.sha256()
        h.update(nonce.to_bytes(4,"big") + (dataToHash))
        hash = h.digest()
        n = int.from_bytes(hash[:4],"big")

        if n >> (32 - bitsToBeZero) == 0:
            print(f"Nonce: {nonce:032b}; Hash: {n:032b}") # TESTES
            break
    #######


    Final = time.time() # Calcular tempo de execução
    tempo = Final - Inicio # Calcular tempo de execução
    return nonce, tempo 
