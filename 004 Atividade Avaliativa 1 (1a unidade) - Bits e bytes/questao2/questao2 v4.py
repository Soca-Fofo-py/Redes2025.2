# Coloque aqui o código de resposta aa questao 2
import os
Dicio_Op = {1:"inicializaRAID",2:"obtemRAID",3:"escreveRAID",4:"leRAID",5:"removeDiscoRAID",6:"constroiDiscoRAID",0:"FinalizaPrograma"} ; opcao = ''
#################################################
def menu ():
    print      (    "\n" + f"{'CÓDIGO':^10s} : AÇÃO QUE DESEJA REALIZAR\n" + 
                    f"{'1':^10s} : InicializaRAID\n" + 
                    f"{'2':^10s} : ObtemRAID\n" + 
                    f"{'3':^10s} : EscreveRAID\n" + 
                    f"{'4':^10s} : LeRAID\n" + 
                    f"{'5':^10s} : RemoveDiscoRAID\n" + 
                    f"{'6':^10s} : ConstroiDiscoRAID\n" + 
                    f"{'< 1 ou > 6':^10s} : Finaliza o programa\n\n" + 
                    "Digite o código da opção que deseja realizar: "
                    )
    try:
        opcao = int (input("Selecione uma opção: "))
        if opcao > 6 or opcao < 1: opcao = 0
        print(f"Opção: {opcao}, {Dicio_Op[opcao]} selecionada.\n")
        return opcao
    except ValueError:
        print("Apenas números inteiros, por favor.")
    except:
        print("Erro inesperado, tente novamente.")
        
dados = {}

def inicializaRAID ():

    dados = {}

    nome_disco = input('dig nome:')

    num_discos = int(input('dig disco:'))
    if num_discos >= 3:
    
        tam_discos = int(input('quantos bytes tera o arquivo:'))
        tam_bloco = int(input('digite o tamanho dos blocos:')) #########
        if tam_bloco  > tam_discos:    
            #tam_bloco = int(input('digite o tamanho dos blocos:'))
            
            quant_blocos = tam_discos//tam_bloco
            
            blocos_max = (tam_discos//tam_bloco)*(len(discos)-1)

            discos = [ nome_disco + str(a) + '.bin' if a != num_discos - 1 else nome_disco + 'x' + '.bin' for a in range (0,num_discos)]

            pasta = input('digite o nome da pasta que voce deseja armazenar os arquivos:')
            
            NADA = 0

            os.mkdir(pasta)

            for a in discos:
                f = open(f'/home/dorbado/Documentos/Faculdade/computaria/{pasta}/{a}','wb')
                f.write(NADA.to_bytes(tam_discos,'big'))
                f.close()
            
            start = 0

            for a in discos:
                blocos = []
                if a != discos[len(discos)-1]:
                    for b in range(start,blocos_max,len(discos)-1):
                        blocos += [b]
        
                    start += 1
                    dados[a] = blocos
            dados['disco_apagado'] = False
            dados['quant_blocos'] = quant_blocos
            dados['tam_bloco'] = tam_bloco
            dados['tam_discos'] = tam_discos
            dados['blocos_max'] = blocos_max
            dados['discos'] = discos
            dados['pasta'] = pasta
                  
        else:
            print('não é possivel ter blocos maior que o disco inteiro')        
    else:
        print('não é possivel fazer raid com menos que três discos') 
    
    return dados
    
def obtemRAID ():
    
    if 'discos' in dados.keys() and 'pasta' in dados.keys():
        exibir_disco = input('qual disco você deseja obter:')
        exibir_pasta = input('em que pasta vc armazenou os discos:')
        if exibir_disco in dados.get('discos') and exibir_pasta == dados.get('pasta'):
            print('o arquivos e a pasta existem')
            
        else:
            if exibir_disco not in dados.get('discos'):
                print('esse disco n existe')
            if exibir_pasta != dados.get('pasta'):
                print('essa pasta n existe')

    else:
        print('você n inicializou o RAID')

def escreveRAID ():
    onde_escrever = int(input('em que byte você quer gravar os seus dados:'))
    bytes = 0
    
    if type(dados.get('tam_discos')) == int and len(dados.get('tam_discos')) * (dados.get('tam_discos')-1) > onde_escrever > 0:
        for a in range(0,dados.get('blocos_max','você ainda n inicializou o raid')):

            bytes += dados.get('tam_bloco')
            if bytes > onde_escrever:
                bloco_escrever = a - 1
                break
        
        
        for a in dados.get('discos'):
            for b in dados.get(dados.get(a)):
                if bloco_escrever in b:
                    disco_escrever = a
                    for c in range(0,len(dados.get(dados.get(a)))):
                        if b[c] == bloco_escrever:
                            byte_escrever = (onde_escrever - (dados.get('tam_discos')*bloco_escrever)) + (dados.get('tam_bloco') * c)
                            byte_bloco = (dados.get('tam_bloco') * c)
                            break

        escrever = int(input('quantos bytes vc deseja ler:'))
        dados_escrever = escrever
        cont = 1
        if escrever < dados.get('tam_bloco') and dados.get('tam_discos')*(len(dados.get('discos'))-1) > escrever and onde_escrever - (dados.get('tam_discos')*(len(dados.get('discos'))-1)) < escrever:
            while dados_escrever != 0:
                for a in range(disco_escrever,len(dados.get('discos')-1)):
                    f = open(f'/home/dorbado/Documentos/Faculdade/computaria/{dados.get('pasta')}/{dados.get('discos')[a]}','rb')
                    if cont == 1:
                        f.seek(byte_escrever)
                    else:
                        f.seek(byte_bloco)
                    if dados_escrever > dados.get('tam_bloco'):
                        if cont > 1:
                            f.write(escrever[((1-cont)*dados.get('tam_bloco')):cont*(dados.get('tam_bloco'))])
                            dados_escrever -= dados.get('tam_bloco')
                            xor_ler(byte_bloco,cont*(dados.get('tam_bloco')),escrever[((1-cont)*dados.get('tam_bloco')):cont*(dados.get('tam_bloco'))])
                        else:
                            dados_escrever -= (byte_escrever - byte_bloco)
                            f.write(escrever[((1-cont)*dados.get('tam_bloco')):(byte_escrever - byte_bloco)])
                            
                            xor_ler(byte_bloco,byte_escrever - byte_bloco,escrever[((1-cont)*dados.get('tam_bloco')):(byte_escrever - byte_bloco)])
                            
                            if byte_escrever == byte_bloco:
                                f.write(escrever[((1-cont)*dados.get('tam_bloco')):dados.get('tam_bloco')])
                                dados_escrever -= (byte_escrever - byte_bloco)
                                xor_ler(byte_bloco,byte_escrever - byte_bloco,escrever[((1-cont)*dados.get('tam_bloco')):(byte_escrever - byte_bloco)])
                    else:
                        f.write(escrever[((1-cont) *dados.get('tam_bloco')):(cont*(dados.get('tam_bloco'))) + dados_escrever])
                        xor_ler(byte_bloco,(cont*(dados.get('tam_bloco'))) + dados_escrever,escrever[((1-cont) *dados.get('tam_bloco')):(cont*(dados.get('tam_bloco'))) + dados_escrever])
                        dados_escrever = 0

                            
                        if a == len(dados.get('discos')) - 1:
                            disco_escrever = 0
                            byte_bloco += dados.get('tam_bloco')
                        cont += 1
                        f.close()
        else:
            f = open(f'/home/dorbado/Documentos/Faculdade/computaria/{dados.get('pasta')}/{disco_escrever}','rb')
            f.seek(byte_escrever)
            f.write(escrever)
            xor_escrever(byte_escrever,byte_escrever+len(escrever),escrever)
            f.close()
            
    else:
        print('o raid ainda n foi iniciado')        
                     
def leRAID ():
    onde_ler = int(input('em que byte você quer gravar os seus dados:'))
    bytes = 0
    
    if type(dados.get('tam_discos')) == int and len(dados.get('tam_discos')) * (dados.get('tam_discos')-1) > onde_ler > 0:
        for a in range(0,dados.get('blocos_max','você ainda n inicializou o raid')):

            bytes += dados.get('tam_bloco')
            if bytes > onde_ler:
                bloco_ler = a - 1
                break
        
        
        for a in dados.get('discos'):
            for b in dados.get(dados.get(a)):
                if bloco_ler in b:
                    disco_ler = a
                    for c in range(0,len(dados.get(dados.get(a)))):
                        if b[c] == bloco_ler:
                            byte_ler = (onde_ler - (dados.get('tam_discos')*bloco_ler)) + (dados.get('tam_bloco') * c)
                            byte_bloco = (dados.get('tam_bloco') * c)
                            break

        ler = input('digite oque vc deseja gravar do disco')
        dados_ler = len(ler)
        cont = 1
        if  len(ler) < dados.get('tam_bloco') and dados.get('tam_discos')*(len(dados.get('discos'))-1) > len(ler) and onde_ler - (dados.get('tam_discos')*(len(dados.get('discos'))-1)) < len(ler):
            while dados_ler != 0:
                for a in range(disco_ler,len(dados.get('discos')-1)):
                    f = open(f'/home/dorbado/Documentos/Faculdade/computaria/{dados.get('pasta')}/{dados.get('discos')[a]}','rb')
                    if cont == 1:
                        f.seek(byte_ler)
                    else:
                        f.seek(byte_bloco)
                    if dados_ler > dados.get('tam_bloco'):
                    
                        if cont > 1:
                            leitura += (f.read(dados.get('tam_bloco'))).decode('utf-8')
                            dados_ler -= dados.get('tam_bloco')
                            xor_leitura += xor_ler(byte_bloco,dados.get('tam_bloco'))
                        
                        else:
                            leitura = (f.read(byte_ler - byte_bloco)).decode('utf-8')
                            dados_ler -= (byte_ler - byte_bloco)
                            xor_leitura = xor_ler(byte_ler , byte_ler - byte_bloco)
                            
                            if byte_ler == byte_bloco:
                                leitura = (f.read(dados.get('tam_bloco'))).decode('utf-8')
                                xor_leitura = xor_ler(byte_bloco,dados.get('tam_bloco'))
                                dados_ler -= (byte_ler - byte_bloco)
                    
                    else:
                        leitura += (f.read(dados_ler)).decode('utf-8')
                        xor_leitura += xor_ler(byte_bloco,dados_ler)
                        dados_ler = 0
                        
                    if a == len(dados.get('discos')) - 1:
                        disco_ler = 0
                        byte_bloco += dados.get('tam_bloco')
                    cont += 1
                    f.close()
            if dados.get('disco_apagado'):
                print(leitura)
            else:
                print(xor_leitura)
        
        else:
            if not(dados.get('disco_apagado')):
                f = open(f'/home/dorbado/Documentos/Faculdade/computaria/{dados.get('pasta')}/{disco_ler}','rb')
                f.seek(byte_ler)
                leitura = f.read(ler)
                print(leitura.decode('utf-8'))
                f.close()
                
                xor_leitura = xor_ler(byte_ler,ler)
                
    else:
        print('o raid ainda n foi iniciado')        
                
def removeDiscoRAID ():
    arquivo_apagado = input('qual dos discos você deseja apagar')
    dados['arquivo_apagado'] = arquivo_apagado
    dados['disco_apagado'] = True
    try:
        os.remove(f'home/dorbado/Documentos/Faculdade/computaria/{dados.get('pasta')}/{arquivo_apagado}')
    except:
        print('não foi possivel a apagar o arquivo')
#wr
def constroiDiscoRAID ():
    if dados.get('disco_apagado'):
        xors = []
        f = open(f'home/dorbado/Documentos/Faculdade/computaria/{dados.get('pasta')}/{dados.get('arquivo_apagado')}','wr')
        f.close()
        for a in range(0,dados.get('quant_blocos')):
            xors = []
            for b in dados.get('discos'):
                if b != dados.get('arquivo_apagado'):
                    f = open(f'home/dorbado/Documentos/Faculdade/computaria/{dados.get('pasta')}/{b}','wr') #wr?
                    f.seek(a * dados.get('tam_bloco'))
                    xors += f.read(dados.get('tam_bloco'))
                    f.close()
            
            for a in range(1,len(xor)):    
                if a < 1:        
                    xor = xor ^ xors[a]
                else:          
                    xor = xors[0] ^ xors[a]
            f = open(f'home/dorbado/Documentos/Faculdade/computaria/{dados.get('pasta')}/{dados.get('arquivo_apagado')}','wr')
            f.seek(a * dados.get('tam_bloco'))
            f.write(xor)
            f.close()
    else:
        print('todos os discos estão inteiros')

# Auxiliares
def xor_ler (start,end):
    xors = []
    for a in dados.get('discos'):
        f = open(f'home/dorbado/Documentos/Faculdade/computaria/{dados.get('pasta')}/{a}','rb')
        f.seek(start)
        xors += f.read(end)
        f.close()
    
    for a in range(1,len(xors)):    
        if a < 1:        
            xor = xor ^ xors[a]
        else:          
            xor = xors[0] ^ xors[a]
    
    if dados.get('disco_apagado'):
        
        return xor.decode('utf-8')

def xor_escrever(start,end,strig):
    xors = [strig]
    if dados.get('disco_apagado'):
        for a in dados.get('discos'):
            if a != dados.get('arquivo_apagado'):
                f = open(f'home/dorbado/Documentos/Faculdade/computaria/{dados.get('pasta')}/{a}','rb')
                f.seek(start)
                xors += f.read(end)
                f.close()
    else:
        for a in dados.get('discos'):
            f = open(f'home/dorbado/Documentos/Faculdade/computaria/{dados.get('pasta')}/{a}','rb')
            f.seek(start)
            xors += f.read(end)
            f.close()

    for a in range(1,len(xor)):    
        if a < 1:        
            xor = xor ^ xor[a]
        else:          
            xor = xor[0] ^ xor[a]
        if dados.get('disco')[len(dados.get['discos'])-1] != dados.get('disco_apagado') :
            f = open(f'home/dorbado/Documentos/Faculdade/computaria/{dados.get('pasta')}/{dados.get('discos')[len(dados.get('discos'))-2]}','rb')
            f.write(xor)
            f.close()
            
def FinalizaPrograma():
    print("Programa finalizado!\n")
#################################################
while opcao != 0:
    opcao = menu()
    #print(Dicio_Op[opcao])
    #funcao = Dicio_Op[opcao]
    #var1 = eval(funcao)()
    funcao = eval(Dicio_Op[opcao])() #######