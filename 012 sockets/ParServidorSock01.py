import socket

Host = ''
Port = 60000

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_socket.bind((Host,Port))

print('recebendo mensagem...\n\n')

while True:
    msg, cliente = udp_socket.recvfrom(1024)
    print(cliente, msg.decode('utf-8'))

    udp_socket.sendto(msg, (cliente))
    
    if msg.decode('utf-8') == 'q':
        break

udp_socket.close()
print('Fim')