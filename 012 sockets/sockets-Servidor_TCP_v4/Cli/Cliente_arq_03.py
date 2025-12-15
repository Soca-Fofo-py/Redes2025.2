import socket , os

Host = '127.0.0.1'
Port = 20000

Codificacao = "utf-8"
Endianess = 'big'
Tam_buffer = 4096
operacoes_disponiveis = [10,"d",20,"l",30,"u"]
solicit = 64 # Recebe n pedidos
meu_diretorio = '.\\MeuEscopo\\'

statusErro = 1 ; statusPositivo = 0 # Duas variáveis para status, em bytes
b_statusErro = statusErro.to_bytes(1,Endianess) ; b_statusPositivo = statusPositivo.to_bytes(1,Endianess)

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect((Host, Port))

try:
    operaçao = input("Digite (10 ou d) para Download, (20 ou l) para listagem ou (30 ou u) para Upload: ")
    try:
        operaçao = int(operaçao)
    except: 
        if operaçao.lower() in operacoes_disponiveis:
            var_op = operaçao.lower()
            if var_op == "d": operaçao = 10
            if var_op == "l": operaçao = 20
            if var_op == "u": operaçao = 30
        else: operaçao = 0
except: operaçao = 0

operaçao_b = operaçao.to_bytes(1,Endianess)
tcp_socket.send(operaçao_b) # Envia operação ao servidor

if operaçao == 10: ####################################################################################################
    nome_arq_str = input ("Digite o nome do arquivo desejado: ") # Lê nome do arquivo
    nome_arq = nome_arq_str.encode(Codificacao) # Nome do arquivo para bytes
    tamanho = len(nome_arq) # Obtem len do nome do arquivo
    tamanho = tamanho.to_bytes(1,Endianess) # tamanho em um byte
    tcp_socket.send(tamanho) # send len do nome
    tcp_socket.send(nome_arq) # send nome
    data = tcp_socket.recv(1) # Recebe o STATUS 0 ou 1 em 1 byte
    data = int.from_bytes(data,Endianess) # byte para inteiro
    print ('Status de: ' , Host , '-->' , data)
    if data == statusPositivo: 
        data = tcp_socket.recv(4) # Recebe tamanho do arquivo
        tam_arq =  int.from_bytes(data,Endianess) # byte para inteiro
        T_a_gravar = tam_arq # Não mexe no tamanho do arquivo / uso futuro
        #bytes_do_arq = b"" # Armazenara os todos os bytes do arquivo
        nome_arq_str = meu_diretorio + nome_arq_str
        with open(f"{nome_arq_str}", "wb") as arquivo : # Escreve arquivo
            while T_a_gravar > 0:
                data = tcp_socket.recv(Tam_buffer)
                arquivo.write(data)
                T_a_gravar -= Tam_buffer
        print("Arquivo baixado em sua totalidade.")
            
    else:
        print("Arquivo não encontrado.")

if operaçao == 20: ####################################################################################################
    status = tcp_socket.recv(1) # Recebe status 0 ou 1
    status = int.from_bytes(status,Endianess)
    if status == statusPositivo: # Se positivo
        tam_listagem = tcp_socket.recv(4) # Recebe len da listagem
        tam_listagem = int.from_bytes(tam_listagem,Endianess)
        listagem = tcp_socket.recv(tam_listagem) # Recebe listagem
        listagem = listagem.decode(Codificacao)
        print(listagem)
    else:
        print(f"Status: {status} recebido.")

if operaçao == 30: ####################################################################################################
    print("Fazer Upload para o servidor")
    nome_arqC = input("Digite o nome do arquivo que deseja enviar ao servidor: ")
    var1 = meu_diretorio + nome_arqC
    print("Tentando enviar: ",nome_arqC)
    if os.path.isfile(var1) == True: # Se arquivo existir:
        tcp_socket.send(b_statusPositivo) # send status positivo
        nome_arqCb = nome_arqC.encode(Codificacao)
        tam_nome_c = len(nome_arqCb)
        tam_nome_c = tam_nome_c.to_bytes(1,Endianess)
        print("Enviando len do nome do arquivo ao servidor.")
        tcp_socket.send(tam_nome_c)
        print("Enviando nome do arquivo ao servidor.")
        tcp_socket.send(nome_arqCb)
        tam_arqC = os.path.getsize(var1) # Obtem tamnho do arquivo
        tam_arq_bC = tam_arqC.to_bytes(4,Endianess) # str para bytes
        tcp_socket.send(tam_arq_bC) # send tamanho do arquivo
        with open (f"{var1}", 'rb') as arquivo:
            while tam_arqC > 0:
                a_enviar = arquivo.read(Tam_buffer)
                tcp_socket.send(a_enviar)
                tam_arqC -= Tam_buffer
        print("Arquivo enviado!")
    else: 
        tcp_socket.send(b_statusErro)
        print("Arquivo NÃO encontrado!")

if operaçao not in operacoes_disponiveis:
    print(operaçao,"Operação invalida!")
tcp_socket.close()
print('Fim Cliente')