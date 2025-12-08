from encodings import utf_8
import socket , os

HOST = '127.0.0.1'
PORT = 20002

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect((HOST, PORT))
operacoes = [10,20]
try:
    operaçao = int(input("Digite 10 para Download ou 20 para Upload: "))
except: operaçao = 0
operaçao_b = operaçao.to_bytes(1,'big')

tcp_socket.send(operaçao_b) # Envia operação ao servidor
if operaçao == 10:

    listagem_tam = tcp_socket.recv(4)
    listagem_tam = int.from_bytes(listagem_tam,"big")
    listagem = tcp_socket.recv(listagem_tam) #recebe listagem
    print(listagem.decode("utf-8"))

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
####################################################################################################
status1 = 1 ; status0 = 0 # Duas variáveis para status, em bytes
status1 = status1.to_bytes(1,'big') ; status0 = status0.to_bytes(1,'big')
if operaçao == 20:
    print("Fazer Upload para o servidor")
    nome_arqC = input("Digite o nome do arquivo que deseja enviar ao servidor: ")

    if os.path.isfile(nome_arqC) == True: # Se arquivo existir:
        tcp_socket.send(status1) # send status 1
        nome_arqCb = nome_arqC.encode("utf-8")
        tam_nome_c = len(nome_arqCb)
        tam_nome_c = tam_nome_c.to_bytes(1,'big')
        print("Enviando len do nome do arquivo ao servidor.")
        tcp_socket.send(tam_nome_c)
        print("Enviando nome do arquivo ao servidor.")
        tcp_socket.send(nome_arqCb)
        tam_arqC = os.path.getsize(nome_arqC) # Obtem tamnho do arquivo
        tam_arq_bC = tam_arqC.to_bytes(4,"big") # str para bytes
        tcp_socket.send(tam_arq_bC) # send tamanho do arquivo
        with open (f"{nome_arqC}", 'rb') as arquivo:
            while tam_arqC > 0:
                a_enviar = arquivo.read(4096)
                tcp_socket.send(a_enviar)
                tam_arqC -= 4096
        print("Arquivo enviado!")
    else: 
        tcp_socket.send(status0)
        print("Arquivo NÃO encontrado!")

else:
    print("Operação invalida!")
tcp_socket.close()
print('Fim Cliente')
