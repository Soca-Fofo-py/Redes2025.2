# Coloque aqui o código de resposta aa questao 1
import findNoncestriong , csv

#    
Textos =[
        "Esse é fácil" , "Esse é fácil" ,"Esse é fácil" ,
        "Texto maior muda o tempo?" , "Texto maior muda o tempo?" , "Texto maior muda o tempo?" ,
        "É possível calcular esse?" , "É possível calcular esse?" , "É possível calcular esse?"
        ]
Bits_em_zero = [8,10,15,8,10,15,18,19,20]
Tabela = [["Texto a validar","Bits em zero","Nonce","Tempo(s)"]]
for pos in range (len(Textos)):
    a = Textos[pos]
    a = bytes(a, "utf-8")
    b = Bits_em_zero[pos]
    #print(a,b)
    valores = [findNoncestriong.findNoncestriong(a,b)]
    print((f"Nonce: {valores[0][0]}; Tempo de execução: {valores[0][1]}s")) # TESTES
    Tabela.append([Textos[pos],Bits_em_zero[pos], valores[0][0], valores[0][1]])
#
for c in Tabela:
    print(c) # TESTES

with open("tabela_csv", "w",newline="") as csv_arq:  
    writer = csv.writer(csv_arq)
    writer.writerows(Tabela)
