from encodings import utf_8
from operator import truediv
import socket

HOST = '127.0.0.1'
PORT = 60000

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input ("Digite a mensagem: ")

    msg = msg.encode('utf-8')

    udp_socket.sendto(msg, (HOST,PORT))


    data, src = udp_socket.recvfrom(1024)
    print ('echo de: ' , src , '-->' , data.decode('utf-8'))
    
    
    if msg.decode('utf-8') == 'q':
        break

udp_socket.close()
print('Fim')
#10.25.1.232
# dir(socket)