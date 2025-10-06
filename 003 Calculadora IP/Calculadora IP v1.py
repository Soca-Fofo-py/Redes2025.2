# 2025.Outubro.05
def bin_to_dec(var):
    
    #decimais = str(tomate[0:8]) +"."+ str(tomate[8:16]) +"."+ str(tomate[16:24]) +"."+ str(tomate[24:32])
    #decimais = [a[0:8],a[8:16],a[16:24],a[24:32]]
    decimais = [ var[0:8],var[8:16],var[16:24],var[24:32] ]
    string_dec = str(int(decimais[0],2)) +'.'+ str(int(decimais[1],2)) +'.'+ str(int(decimais[2],2)) +'.'+ str(int(decimais[3],2))

    return string_dec




ip_source =  '10.14.11.10' #input("Digite o endereço IP no seguinte formato: 192.168.10.5\nEndereço IP: ") #
net_mask = 16 #int(input("Digite a mascara da rede no seguinte formato: 24\nMascara da rede: ")) #

hosts = 32-net_mask
print(f'Rede: {ip_source}\nMask: {net_mask}')#######

ip_lista = [int(x) for x in ip_source.split(".")]
print("IP Lista: ",ip_lista)#######

ip_bytes = bytes(ip_lista)
print("IP Bytes: ",ip_bytes,"Pos[0]:",ip_bytes[0:3])#######

ip_int_grande = int.from_bytes(ip_bytes)
print("IP IntGrade: ",ip_int_grande)#######


ip_rede = ip_int_grande >> hosts << hosts
print("IP Rede",ip_rede)#######

ip_broadcast = ip_rede | ((1<<hosts)-1)
print("IP Broadcast",ip_broadcast)#######

end_gateway = ip_rede | 1
print("Endereço Gateway: ",end_gateway)#######

endereços_validos = (2**(hosts)) - 2
print("Endereços váilidos: ",endereços_validos)#######

'''
area_host = ((1 << hosts) - 1)
print(f'{area_host:032b}')
print(area_host & ip_int_grande)
'''
#print(f"TEST{(1<<32)-1:032b}")
print()

ip_rede_dec = str((f'{ip_rede:032b}'))
ip_broadcast_dec = str((f'{ip_broadcast:032b}'))
end_gateway_dec = str((f'{end_gateway:032b}'))
#print(f'{ip_rede_dec}\n{ip_broadcast_dec}\n{end_gateway_dec}')


print(f"{'Endereço IP da Rede:':<32} {ip_rede:032b} -> {bin_to_dec(ip_rede_dec)}\n"
      f"{'Endereço IP de broadcast:':<32} {ip_broadcast:032b} -> {bin_to_dec(ip_broadcast_dec)}\n"
      f"{'Endereço IP de Gateway(Comum):':<32} {end_gateway:032b} -> {bin_to_dec(end_gateway_dec)}\n"
      f"Quantidade de endereços válidos para hosts: {endereços_validos}"
      ) 

'''
tomate = str((f'{ip_rede:032b}'))
print(tomate)
lista_tomate = [tomate[0:8],tomate[8:16],tomate[16:24],tomate[24:32]]
print(bin_to_dec(tomate))
'''



# Fontes:
# https://www.gta.ufrj.br/grad/99_1/fernando/roteamento/classes.htm
