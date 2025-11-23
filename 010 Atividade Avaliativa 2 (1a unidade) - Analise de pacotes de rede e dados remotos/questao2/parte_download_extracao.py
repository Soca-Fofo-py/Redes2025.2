import funcoes , requests , zipfile , struct , os , sys

print('O URL do arquivo desejado pode ser encontrado no seguinte website: https://malware-traffic-analysis.net')
global url_requisitada
url_requisitada = 'https://malware-traffic-analysis.net/2020/07/13/2020-07-13-Dridex-infection-traffic.pcap.zip' #input("Digite a URL do arquivo desejado: ")
# https://malware-traffic-analysis.net/2020/07/13/index2.html TESTES

# Request e escreve ZIP no disco
try:
    r = requests.get(url_requisitada)
    if r.status_code == 200:
        dados_a_escrever = r.content
        funcoes.escreve_no_disco(dados_a_escrever,url_requisitada)
        #print("Fim do laço download e escrita.")
    else: print('Erro! Resposta diferente de: 200 OK')
except: print("Erro!", ValueError)

# Desempacota
funcoes.desempacota(url_requisitada)
print("Desempacotado com sucesso.")

# Lê arquivo .pcap
