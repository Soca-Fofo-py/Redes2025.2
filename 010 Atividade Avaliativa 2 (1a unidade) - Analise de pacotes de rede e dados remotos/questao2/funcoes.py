def obtem_nome(url_requisitada):

    nomeArquivo = (url_requisitada[url_requisitada.rfind('/')+1:]) # './' +  (var[var.rfind('/')+1:])
    #print(nomeArquivo)
    return nomeArquivo
# Concluido

def escreve_no_disco(dados_a_escrever,url_requisitada):
    
    with open(obtem_nome(url_requisitada), 'wb') as arq:
        arq.write(dados_a_escrever)
        print(f"Arquivo escrito no disco como: {obtem_nome(url_requisitada)}")
# Concluido

def obtem_senha(url_requisitada):
    # infected_AAAAMMDD
    nome_arq = obtem_nome(url_requisitada)
    lista = nome_arq.split("-")
    senha = 'infected_' + lista[0] + lista[1] + lista[2]
    print(f"Asenha é: {senha}")
    return senha
# Concluido

def desempacota(url_requisitada):
    print("Desempacotando...")
    import zipfile
    senhab = bytes(obtem_senha(url_requisitada), 'utf-8')
    try:
        with zipfile.ZipFile(obtem_nome(url_requisitada),'r') as arq:
            nomeunzip = obtem_nome(url_requisitada)[:len(obtem_nome(url_requisitada))-4]
            arq.setpassword(senhab)
            arq.extractall('.') #nomeunzip
        print("Arquivo extraido como: ",nomeunzip)
    except: print("Erro.",ValueError)
# Concluido

# Trabalhando com arquivo .pcap
def check_endianess(b_endianness):
    if b_endianness == b'\xd4\xc3\xb2\xa1' or b_endianness == b'\xd4\x3c\xb2\xa1':
        endianness  = 'little'
        return endianness
    else:
        if b_endianness == b'\xa1\xb2\xc3\xd4' or b_endianness == b'\xa1\xb2\x3c\xd4': 
            endianness  = 'big'
            return endianness
        else: 
            print("Não é um aquivo .pcap")
            endianness = 0
            return endianness
# Concluido

def check_time(b_endianness):
    if b_endianness == b'\xd4\xc3\xb2\xa1' or b_endianness == b'\xa1\xb2\x3c\xd4': #
        time_in  = 'micro_sec'
        return time_in
    else:
        if b_endianness == b'\xa1\xb2\xc3\xd4' or b_endianness == b'\xd4\x3c\xb2\xa1': 
            time_in  = 'nano_sec'
            return time_in
        else: 
            print("Não é um aquivo .pcap")
            time_in = 0
            return time_in
# Concluido

def exibe_header_IP(header_IP,endianness): # Exibe header IP e retorna protocolo carregado
    #print(header_IP)
    # Do material de aula
    print("Header IP: ")
    print (f"Versão:  {header_IP[0]>>4} | hlen = {header_IP[0] & ((1 << 4) - 1)} 'Vezes 4' ")
    print (f"Total Length:  {(int.from_bytes(header_IP[2:4],byteorder=endianness))} | TTL: {header_IP[8]} | Protocolo: {header_IP[9]}")
    print (f"IP-Origem:  {header_IP[12]}.{header_IP[13]}.{header_IP[14]}.{header_IP[15]}",end=" | ")
    print (f"IP-Destino: {header_IP[16]}.{header_IP[17]}.{header_IP[18]}.{header_IP[19]}\n")
    #print (f"test: {(int.from_bytes(header_IP[0:2],byteorder='little')>>4)}")
    IP_origem = f'{header_IP[12]}.{header_IP[13]}.{header_IP[14]}.{header_IP[15]}'
    IP_destino = f'{header_IP[16]}.{header_IP[17]}.{header_IP[18]}.{header_IP[19]}'
    par_IP = [IP_origem,IP_destino]
    protocolo = header_IP[9]
    return protocolo ,par_IP
# Concluido

def processa_UDP(header_UDP,endianness):
    #print(header_UDP)
    tam_pac_UDP = (int.from_bytes(header_UDP[4:],byteorder=endianness))
    #print(tam_pac_UDP)
    return tam_pac_UDP
# Concluido
