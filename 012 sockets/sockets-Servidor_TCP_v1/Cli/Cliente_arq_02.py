from encodings import utf_8
import socket

HOST = '127.0.0.1'
PORT = 60000

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect((HOST, PORT))

nome_arq_str = input ("Digite o nome do arquivo desejado: ") # Lê nome do arquivo
nome_arq = nome_arq_str.encode('utf-8') # Nome do arquivo para bytes

tamanho = len(nome_arq) # Obtem len do nome do arquivo
tamanho = tamanho.to_bytes(1,'big') # tamanho em um byte

tcp_socket.send(tamanho) # send len do nome
tcp_socket.send(nome_arq) # send nome

data = tcp_socket.recv(1) # Recebe o STATUS 0 ou 1 em 1 byte
data = int.from_bytes(data,"big") # byte para inteiro
print ('Status de: ' , HOST , '-->' , data)

if data == 1: 
    data = tcp_socket.recv(4) # Recebe tamanho do arquivo
    tam_arq =  int.from_bytes(data,'big') # byte para inteiro
    T_a_gravar = tam_arq # Não mexe no tamanho do arquivo / uso futuro
    #bytes_do_arq = b"" # Armazenara os todos os bytes do arquivo
    with open(f"{nome_arq_str}", "wb") as arquivo : # Escreve arquivo
        while T_a_gravar > 0:
            data = tcp_socket.recv(4096)
            arquivo.write(data)
            T_a_gravar -= 4096
    print("Arquivo baixado em sua totalidade.")
        
else:
    print("Arquivo não encontrado.")

tcp_socket.close()
print('Fim Cliente')
