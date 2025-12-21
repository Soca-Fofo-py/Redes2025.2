import socket , os 
import funcaoDicio

####################################################################################################
ips_ser = [addr[4][0] for addr in socket.getaddrinfo(socket.getfqdn(), 80, socket.AF_INET)]
for ip in ips_ser:
	print (f"Escutando em: {ip}:20000")
####################################################################################################

Host = ''
Port = 20000

Codificacao = "utf-8"
Endianess = 'big'
Tam_buffer = 4096
operacoes_disponiveis = [10,20,30]
solicit = 64 # Recebe n pedidos
meu_diretorio = '.\\MeuEscopo\\'

statusErro = 1 ; statusPositivo = 0 # Duas variáveis para status, em bytes
b_statusErro = statusErro.to_bytes(1,Endianess) ; b_statusPositivo = statusPositivo.to_bytes(1,Endianess)

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((Host,Port))
tcp_socket.listen(1)

while solicit > 0:
    print('On-line...Esperando...')
    con, cliente = tcp_socket.accept() # Aceeita conexão
    print(f"Conectado por: ",cliente)
    print("Esperando operação...")
    opera_a_exe = con.recv(1) # Recebe operação
    opera_a_exe = int.from_bytes(opera_a_exe,Endianess)
    if opera_a_exe == 10: ####################################################################################################
        print("Status OP:",opera_a_exe,"Enviar para o cliente.")
        print("Esperando len do nome do arquivo...")
        Tam_nome_arq = con.recv(1) # Recebe len do nome
        Tam_nome_arq = int.from_bytes(Tam_nome_arq,Endianess) # byte para inteiro
        print("len do nome do arquivo requisitado: ", Tam_nome_arq)
        print("Esperando nome do arquivo...")
        nome_arq = con.recv(Tam_nome_arq) # Recebe nome do arquivo
        nome_arq = nome_arq.decode(Codificacao) # bytes para str
        print("Arquivo requisitado: ", nome_arq)
        nome_arq = meu_diretorio + nome_arq # Nome a partir do escopo
        try: 
            if os.path.isfile(nome_arq) == True: # Se arquivo existir:
                con.send(b_statusPositivo) # send status 1
                tam_arq = os.path.getsize(nome_arq) # Obtem tamnho do arquivo
                tam_arq_b = tam_arq.to_bytes(4,Endianess) # str para bytes
                con.send(tam_arq_b) # send tamanho do arquivo
                with open (f"{nome_arq}", 'rb') as arquivo:
                    while tam_arq > 0:
                        a_enviar = arquivo.read(Tam_buffer)
                        con.send(a_enviar)
                        tam_arq -= Tam_buffer
                print("Arquivo enviado!")
                con.close()
            else: 
                con.send(b_statusErro)
                print("Arquivo NÃO encontrado!")
                con.close()
        except:
            con.send(b_statusErro)
            print("Arquivo NÃO encontrado ou ERRO inesperado.")
            con.close()
        solicit -= 1
    if opera_a_exe == 20: ####################################################################################################
        try:
            print("Preparando a listagem...")
            lista , tamanho_lis_b = funcaoDicio.f_dicio_to_json(meu_diretorio)
            lista_b = lista.encode(Codificacao)
            con.send(b_statusPositivo) # Envia status 0
            print("Enviando len da listagem...")
            con.send(tamanho_lis_b) # Envia len da listagem
            print("Enviando a listagem...")
            con.send(lista_b) # Envia listagem
            con.close()
        except: 
            con.send(b_statusErro) # Envia status 0
            con.close()
    if opera_a_exe == 30: ####################################################################################################
        print("Status OP:",opera_a_exe,"Tentando receber arquivo do cliente.")
        #statusDoCli = con.recv(1)
        #statusDoCli = int.from_bytes(statusDoCli,Endianess)
        #print("Status do vindo do cliente:",statusDoCli)
        #if statusDoCli == statusPositivo: # Se positivo
        print("Recebendo len do nome do arquivo...")
        len_do_nomeC = con.recv(4)
        len_do_nomeC = int.from_bytes(len_do_nomeC,Endianess)
        print("Recebendo nome do arquivo...")
        nome_do_arqC = con.recv(len_do_nomeC)
        nome_do_arqC = nome_do_arqC.decode(Codificacao)
        nome_do_arqC = meu_diretorio + nome_do_arqC
        if len_do_nomeC != 0: # Posso mudar condição
            con.send(b_statusPositivo)
            print("Recebendo tamanho do arquivo...")
            tamanho = con.recv(4)
            tamanho = int.from_bytes(tamanho,Endianess)
            print("Escrevendo no disco...")
            try:
                with open(f"{nome_do_arqC}", "wb") as arquivo : # Escreve arquivo no disco
                    while tamanho > 0:
                        data = con.recv(Tam_buffer)
                        arquivo.write(data)
                        tamanho -= Tam_buffer
                con.send(b_statusPositivo)
                print("Arquivo baixado do cliente em sua totalidade.")
            except:
                print("Erro inesperado.")
                con.send(b_statusErro)
        else:
            print("Arquivo não aceito.")
            con.send(b_statusErro)
        con.close()

        #else: 
            #print("Status vindo do cliente:",statusDoCli)
            #print("cliente tentou enviar algo inexsitente/Invalido")
            #con.close()
    if opera_a_exe not in operacoes_disponiveis:
        print("Status OP:",opera_a_exe,"Operação invalida!")
tcp_socket.close()
print('Fim Servidor')