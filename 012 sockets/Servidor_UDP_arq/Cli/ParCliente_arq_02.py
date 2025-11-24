from encodings import utf_8

import socket , os # os.path.getsize

HOST = '127.0.0.1'
PORT = 60000

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


nome_arq = input ("Digite o nome do arquivo desejado: ")

nome_arq = nome_arq.encode('utf-8')
tamanho = len(nome_arq)
tamanho = tamanho.to_bytes(1,'big')

udp_socket.sendto(tamanho, (HOST,PORT)) # send len do nome
udp_socket.sendto(nome_arq, (HOST,PORT)) # send nome

data, src = udp_socket.recvfrom(1) # STATUS
print ('Status de: ' , src , '-->' , data.decode('utf-8'))
if data.decode('utf-8') == 1: 
    data, src = udp_socket.recvfrom(4) # recv Tamanho do arquivo
    tam_arq =  int.from_bytes(data,'big')
    T_a_gravar = tam_arq
    bytes_do_arq = ''
    while T_a_gravar >=0:
        data, src = udp_socket.recvfrom(4096)
        bytes_do_arq += data
        T_a_gravar -= 4096
        
    with open(f"{nome_arq}", "wb") as arquivo :
        arquivo.write(T_a_gravar)
            



else:
    print("Arquivo não encontrado.")


udp_socket.close()
print('Fim')
