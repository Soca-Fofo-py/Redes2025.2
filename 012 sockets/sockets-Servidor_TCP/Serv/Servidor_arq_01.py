import socket , os 

Host = ''
Port = 60000

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((Host,Port))
tcp_socket.listen(1)

status1 = 1 ; status0 = 0 # Duas variáveis para status, em bytes
status1 = status1.to_bytes(1,'big') ; status0 = status0.to_bytes(1,'big')
solicit = 64 # Recebe n pedidos

while solicit > 0:
    print('On-line...Esperando...')

    con, cliente = tcp_socket.accept() # Aceeita conexão
    print(f"Conectado por: ",cliente)

    print("Esperando len do nome do arquivo...")
    Tam_nome_arq = con.recv(1) # Recebe len do nome
    Tam_nome_arq = int.from_bytes(Tam_nome_arq,"big") # byte para inteiro
    print("len do nome do arquivo requisitado: ", Tam_nome_arq)
    print("Esperando nome do arquivo...")
    nome_arq = con.recv(Tam_nome_arq) # Recebe nome do arquivo
    nome_arq = nome_arq.decode("utf-8") # bytes para str
    print("Arquivo requisitado: ", nome_arq)

    try: 
        if os.path.isfile(nome_arq) == True: # Se arquivo existir:
            con.send(status1) # send status 1
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
            con.send(status0)
            solicit -=1
            print("Arquivo NÃO encontrado!")
            con.close()
    except:
        con.send(status0)
        solicit -=1
        print("Arquivo NÃO encontrado ou ERRO inesperado.")
        con.close()

tcp_socket.close()
print('Fim Servidor')
