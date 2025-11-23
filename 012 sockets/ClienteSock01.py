from encodings import utf_8
import socket

HOST = '10.25.1.232'
PORT = 60000

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = input ("Digite a mensagem: ")

msg = msg.encode('utf-8')

udp_socket.sendto(msg, (HOST,PORT))


data, src = udp_socket.recvfrom(1024)
print ('echo de: ' , src , '-->' , data.decode('utf-8'))


udp_socket.close()
#10.25.1.232
# dir(socket)