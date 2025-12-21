
Host = '127.0.0.1'
Port = 20000

Codificacao = "utf-8"
Endianess = 'big'
Tam_buffer = 4096
operacoes_disponiveis = [10,"d",20,"l",30,"u"]
solicit = 64 # Recebe n pedidos
meu_diretorio = '.\\MeuEscopo\\'

statusErro = 1 ; statusPositivo = 0 # Duas variáveis para status, em bytes
b_statusErro = statusErro.to_bytes(1,Endianess) ; b_statusPositivo = statusPositivo.to_bytes(1,Endianess)

try:
    operaçao = input("Digite (10 ou d) para Download, (20 ou l) para listagem ou (30 ou u) para Upload: ")
    try:
        print("Tenta inteiro")
        operaçao = int(operaçao)
        print("Conseguiu inteiro",operaçao)
    except: 
        print("Não é inteiro: ",operaçao)
        print("Entra excessão dos inteiros")
        #try:
        print("STR: ",operaçao.lower())
        if operaçao.lower() in operacoes_disponiveis:
            var_op = operaçao.lower()
            print("Em operações disponiveis:",operaçao.lower())
            if var_op == "d": operaçao = 10
            if var_op == "l": operaçao = 20
            if var_op == "u": operaçao = 30
        else: operaçao = 0 ; print("Não está em operações disponiveis. 01")
        #except: operaçao = 0 ; print("Não está em operações disponiveis. 02")
except: operaçao = 0 ; print("Não está em operações disponiveis. 03")

operaçao_b = operaçao.to_bytes(1,Endianess)
print("Operação final",operaçao)
print("Operação final em um byte",operaçao_b)