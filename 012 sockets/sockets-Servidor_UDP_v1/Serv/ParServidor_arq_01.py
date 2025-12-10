
import socket , os

Host = ''
Port = 60000

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_socket.bind((Host,Port))

print('On-line...\n\n')
status1 = 1 ; status0 = 0 
status1 = status1.to_bytes(1,'big') ; status0 = status0.to_bytes(0,'big')

while True:
    Tam_nome_arq, cliente = udp_socket.recvfrom(1) # len nome
    #print(cliente, msg.decode('utf-8'))
    var = int.from_bytes(Tam_nome_arq,'big')

    nome_arq, cliente = udp_socket.recvfrom(var) # nome arq

    try: 
        if os.path.isfile(nome_arq.decode('uft-8')) == True:
            udp_socket.sendto(status1, (cliente)) # send status
            tam_arq = os.path.getsize(nome_arq.decode('utf-8'))
            tam_arq_b = tam_arq.to_bytes(4,"big") # send tamanho do arquivo
            udp_socket.sendto(tam_arq_b, (cliente))

            with open (f"{nome_arq}", 'rb') as arquivo:
                while tam_arq >= 0:
                    a_enviar = arquivo.read(4096)
                    tam_arq -= 4096
                    udp_socket.sendto(a_enviar, (cliente))
            
    
    
    except:
        udp_socket.sendto(status0, (cliente))

    udp_socket.close()
    print('Fim')
    
    




