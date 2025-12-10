import socket , os 
import funcaoDicio
Host = ''
Port = 20000

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((Host,Port))
tcp_socket.listen(1)

operacoes_disponiveis = [10,20,30]
status1 = 1 ; status0 = 0 # Duas variáveis para status, em bytes
status1 = status1.to_bytes(1,'big') ; status0 = status0.to_bytes(1,'big')
solicit = 64 # Recebe n pedidos


#meu_diretorio = ".\\012 sockets\\sockets-Servidor_TCP_v2\\Serv\\"
meu_diretorio = '.\\MeuEscopo\\' 

while solicit > 0:
    print('On-line...Esperando...')

    con, cliente = tcp_socket.accept() # Aceeita conexão
    print(f"Conectado por: ",cliente)
    print("Esperando operação...")
    opera_a_exe = con.recv(1) # Recebe operação
    opera_a_exe = int.from_bytes(opera_a_exe,"big")
    

    if opera_a_exe == 10: ####################################################################################################
        print("Status OP:",opera_a_exe,"Enviar para o cliente.")
        
        print("Esperando len do nome do arquivo...")
        Tam_nome_arq = con.recv(1) # Recebe len do nome
        Tam_nome_arq = int.from_bytes(Tam_nome_arq,"big") # byte para inteiro
        print("len do nome do arquivo requisitado: ", Tam_nome_arq)
        print("Esperando nome do arquivo...")
        nome_arq = con.recv(Tam_nome_arq) # Recebe nome do arquivo
        nome_arq = nome_arq.decode("utf-8") # bytes para str
        print("Arquivo requisitado: ", nome_arq)

        nome_arq = meu_diretorio + nome_arq
        try: 
            if os.path.isfile(nome_arq) == True: # Se arquivo existir:
                con.send(status0) # send status 1
                tam_arq = os.path.getsize(nome_arq) # Obtem tamnho do arquivo
                tam_arq_b = tam_arq.to_bytes(4,"big") # str para bytes
                con.send(tam_arq_b) # send tamanho do arquivo
                solicit -=1
                with open (f"{nome_arq}", 'rb') as arquivo:
                    while tam_arq > 0:
                        a_enviar = arquivo.read(4096)
                        con.send(a_enviar)
                        tam_arq -= 4096
                print("Arquivo enviado!")
                con.close()
            else: 
                con.send(status1)
                solicit -=1
                print("Arquivo NÃO encontrado!")
                con.close()
        except:
            con.send(status1)
            solicit -=1
            print("Arquivo NÃO encontrado ou ERRO inesperado.")
            con.close()
    if opera_a_exe == 20: ####################################################################################################
        try:
            print("Preparando a listagem...")
            lista , tamanho_lis_b = funcaoDicio.f_dicio_to_json(meu_diretorio)
            lista_b = lista.encode("utf-8")
            con.send(status0) # Envia status 0
            print("Enviando len da listagem...")
            con.send(tamanho_lis_b) # Envia len da listagem
            print("Enviando a listagem...")
            con.send(lista_b) # Envia listagem
            con.close()
        except: 
            con.send(status1) # Envia status 0
            con.close()

    if opera_a_exe == 30: ####################################################################################################
        print("Status OP:",opera_a_exe,"Tentando receber arquivo do cliente.")
        statusDoCli = con.recv(1)
        statusDoCli = int.from_bytes(statusDoCli,'big')
        print("Status do vindo do cliente:",statusDoCli)
        if statusDoCli == 0:
            print("Recebendo len do nome do arquivo...")
            len_do_nomeC = con.recv(1)
            len_do_nomeC = int.from_bytes(len_do_nomeC,'big')
            print("Recebendo nome do arquivo...")
            nome_do_arqC = con.recv(len_do_nomeC)
            nome_do_arqC = nome_do_arqC.decode("utf-8")
            nome_do_arqC = meu_diretorio + nome_do_arqC
            print("Recebendo tamanho do arquivo...")
            tamanho = con.recv(4)
            tamanho = int.from_bytes(tamanho,'big')
            print("Escrevendo no disco...")
            with open(f"{nome_do_arqC}", "wb") as arquivo : # Escreve arquivo
                while tamanho > 0:
                    data = con.recv(4096)
                    arquivo.write(data)
                    tamanho -= 4096
            print("Arquivo baixado do cliente em sua totalidade.")
            con.close()
        else: 
            print("Status vindo do cliente:",statusDoCli)
            print("cliente tentou enviar algo inexsitente/Invalido")
            con.close()

    if opera_a_exe not in operacoes_disponiveis:
        print("Status OP:",opera_a_exe,"Operação invalida!")
tcp_socket.close()
print('Fim Servidor')
