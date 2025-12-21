import socket


ips = [addr[4][0] for addr in socket.getaddrinfo(socket.getfqdn(), 80, socket.AF_INET)]
for ip in ips:
	print (f"Escutando em: {ip}:5123")
