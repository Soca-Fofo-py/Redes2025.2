# Coloque aq# Coloque aqui o código de resposta aa questao 2

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


# inicializaRAID: Pergunta ao usuário quantos discos serão utilizados em RAID, o tamanho dos discos (o mesmo para todos) 
# e o tamanho do bloco. Os arquivos devem ser criados em uma pasta que o usuário também deve informar.
def inicializaRAID():
    print("Teste 001")


# obtemRAID: Essa operação pergunta ao usuário as mesmas informações de InicializaRAID, mas em vez criar os arquivos, 
# busca os arquivos criados anteriormente com inicializaRAID;
def obtemRAID():
    print("Teste 002")


# escreveRAID: Pergunta ao usuário um conjunto de dados a gravar no RAID e a posição onde iniciar a gravação. 
# Essa posição pode ser qualquer valor entre zero e o tamanho lógico do RAID -1. Por exemplo, se o RAID tem cinco discos 
# (quatro de dados e um de paridade) e o tamanho dos discos é 10000 bytes, então a posição pode ser qualquer valor entre 0 e 39999. 
# O programa deve identificar em que arquivo(s) gravar os dados e que posição dentro do(s) arquivo(s).
# Após a escrita no arquivo correto, o disco de paridade deve ser atualizado;
def escreveRAID():
    print("Teste 003")


# leRAID: Pergunta ao usuário informações sobre dados a ler do RAID. O usuário informa a posição e quantos bytes ler. 
# A lógica para encontrar o arquivo de onde ler é a mesma da escrita. A paridade não necessita ser atualizada;
def leRAID():
    print("Teste 004")


# removeDiscoRAID: O usuário indica um disco a remover do RAID4 (simulando um defeito). O arquivo que representa o disco deve ser apagado pelo programa. 
# Ainda assim, as operações seguintes de leitura e escrita devem operar normalmente, mesmo quando envolvem o disco removido.
# Quando a leitura envolve o disco removido, os dados devem ser obtidos mediante xor nos demais discos e no disco de paridade. A operação de escrita no  disco
# removido gera efeitos apenas no disco de paridade, a fim de permitir (indiretamente) que os dados sendo gravados possam ser recuperados em futuras leituras;
def removeDiscoRAID():
    print("Teste 005")


# constroiDiscoRAID: O usuário pede para reconstruir o disco defeituoso. 
# Um novo arquivo deve ser criado e ter seu conteúdo gerado a partir dos discos remanescentes e o disco de paridade.
def constroiDiscoRAID():
    print("Teste 006")


def FinalizaPrograma():
    print("Programa finalizado!\n")
#################################################
while opcao != 0:
    opcao = menu()

    #print(Dicio_Op[opcao])
    #funcao = Dicio_Op[opcao]
    #var1 = eval(funcao)()
    funcao = eval(Dicio_Op[opcao])() #######ui o código de resposta aa questao 2
