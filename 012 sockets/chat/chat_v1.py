import socket , threading
from tkinter import Menu


IP = "10.25.2.0"
PORTA = 12345
CODIFICACAO = "utf-8"
ENDIANESS = "big"

sock_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_cliente.connect((IP,PORTA))


def receber (sock_cliente):
    tam_mensagem_a_exibir = sock_cliente.recv(4)
    tam_mensagem_a_exibir = int.from_bytes(tam_mensagem_a_exibir,ENDIANESS)

    mensagem_a_exibir = (sock_cliente.recv(tam_mensagem_a_exibir)).decode(CODIFICACAO)
    print(mensagem_a_exibir)

threading.Thread(target=receber, args=(sock_cliente)).start()


while True:
    mensagem = input("Digite uma mensagem a ser enviada: ")
    if mensagem == "q!": 
        sock_cliente.close()
        break
    mensagem_b = mensagem.encode(CODIFICACAO)
    tam_mens = len (mensagem_b).to_bytes(4,ENDIANESS)
    print (tam_mens)

    sock_cliente.send(tam_mens)
    sock_cliente.send(mensagem_b)
