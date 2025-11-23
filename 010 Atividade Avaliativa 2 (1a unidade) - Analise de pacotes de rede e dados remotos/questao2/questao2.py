import funcoes , requests

print('O URL do arquivo desejado pode ser encontrado no seguinte website: https://malware-traffic-analysis.net')
global url_requisitada
url_requisitada = 'https://malware-traffic-analysis.net/2020/07/13/2020-07-13-Dridex-infection-traffic.pcap.zip' #input("Digite a URL do arquivo desejado: ")
# https://malware-traffic-analysis.net/2020/07/13/index2.html TESTES
codigo = 0
# Request e escreve ZIP no disco
try:
    r = requests.get(url_requisitada)
    if r.status_code == 200:
        dados_a_escrever = r.content
        funcoes.escreve_no_disco(dados_a_escrever,url_requisitada)
        codigo = 1
        #print("Fim do laço download e escrita.")
    else: print('Erro! Resposta diferente de: 200 OK')
except: print("Erro!", ValueError)

# Desempacota
funcoes.desempacota(url_requisitada)
print("Desempacotado com sucesso.")
##########################################################################################
# Lê arquivo .pcap
if codigo == 1:
    try:
        nomeArquivo = (url_requisitada[url_requisitada.rfind('/')+1:])
        nomeunzip = nomeArquivo[:len(nomeArquivo)-4]

        with open (nomeunzip,'rb') as arq_pcap:

            b_endianness = arq_pcap.read(4) 
            endianness = funcoes.check_endianess(b_endianness) 
            timesec = funcoes.check_time(b_endianness)
            print('Endianness:',endianness,' | Tempo em:',timesec)

            # Variaveis a usar
            maior_TCP = 0 ; pacotes_incompletos = 0 ; media_UDP = [] ; trafegos_IP = {}

            if endianness != 0:
                arq_pcap.seek(20,1)

                var_1 = 0 # Para de tentar ler quando o arquivo acabar
                while var_1 != b'':
                    arq_pcap.seek(8,1) # Pula dois campos do pac header
                    tam_pacote = int.from_bytes(arq_pcap.read(4),byteorder=endianness)  # Tamanho do pacote
                    tam_pacote_original = int.from_bytes(arq_pcap.read(4),byteorder=endianness)  # Tamanho do pacote original
                    
                    if tam_pacote != tam_pacote_original: # Pacotes não capturados por completo
                        pacotes_incompletos += 1
                    
                    arq_pcap.seek(12,1) # Pula mac addresses
                    var_1 = arq_pcap.read(2) # bytes do type

                    if var_1 == b'\x08\x00':
                        t = arq_pcap.read(2)
                        t = int.from_bytes(t,byteorder=endianness)
                        if t == 69: # Se é IP
                            arq_pcap.seek(-2,1)
                            header_IP = arq_pcap.read(20)
                            protocolo,par_IP = funcoes.exibe_header_IP(header_IP,endianness) # Exibe header
                            
                            trafegos_IP[f'{par_IP}'] = trafegos_IP.get(f'{par_IP}',0) + tam_pacote -14

                            if protocolo == 17:
                                #print("É UDP")
                                pacote_UDP = arq_pcap.read(6)
                                media_UDP.append(funcoes.processa_UDP(pacote_UDP,endianness))
                                
                                arq_pcap.seek(-6,1)

                            if protocolo == 6:
                                #print("É TCP")
                                tam_pac_TCP = tam_pacote - 14 # Menos ethernet header

                                if tam_pac_TCP > maior_TCP:
                                    maior_TCP = tam_pac_TCP
                                
                            arq_pcap.seek(-20,1)

                        arq_pcap.seek(-14,1)

                    else:
                        arq_pcap.seek(-14,1)
                        '''
                        if var_1 != b'' :
                            print('Não é pacote IP')'''
                    arq_pcap.seek(tam_pacote,1)
                    #break
                soma = 0 # Media dos pacotes UDP
                for g in media_UDP:
                    soma += g
                media = soma/len(media_UDP)
                print('Tamanho do maior pacote TCP: ',maior_TCP)
                print("Pacotes que não foram salvos nas suas totalidades: ", pacotes_incompletos)
                print(f"A media dos pacotes UDPs é: {int(media)}, Provenientes de {len(media_UDP)} pacote/s.")
                maior_trafego = max(trafegos_IP , key=trafegos_IP.get)
                print(f"O maior trafego foi gerado per: {maior_trafego}, com tamanho: {trafegos_IP[maior_trafego]}")
                print("Diferentes pacotes Origem-Destino IPs capturados: ", len(trafegos_IP)) # Dividir por 2
                print('FIM')
    except: print("Erro: ",ValueError)