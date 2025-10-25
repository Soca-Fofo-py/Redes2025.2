# Coloque aqui o código de resposta a questao 1
import findNonce , csv

#######
Textos =[
        "Esse é fácil" , "Esse é fácil" ,"Esse é fácil" ,
        "Texto maior muda o tempo?" , "Texto maior muda o tempo?" , "Texto maior muda o tempo?" ,
        "É possível calcular esse?" , "É possível calcular esse?" , "É possível calcular esse?"
        ]
Bits_em_zero = [8,10,15,8,10,15,18,19,20]
Tabela = [["Texto a validar","Bits em zero","Nonce","Tempo(s)"]]

#######
for pos in range (len(Textos)):
    a = Textos[pos]
    a = bytes(a, "utf-8")
    b = Bits_em_zero[pos]
    # Chama a função com os valores na lista "Textos" e "Bits_em_zero" determinados no enunciado e coloca os retornos em "valores".
    valores = [findNonce.findNonce(a,b)]
    print((f"Nonce: {valores[0][0]}; Tempo de execução: {valores[0][1]}s")) # TESTES
    # Coloca os 4 volores como um elemento na lista "Tabela"
    Tabela.append([Textos[pos],Bits_em_zero[pos], valores[0][0], valores[0][1]])

#######
for c in Tabela: # TESTES
    print(c) # TESTES

with open("tabela_csv", "w",newline="") as csv_arq:  
    writer = csv.writer(csv_arq)
    writer.writerows(Tabela)
    # Coloca um valor de "Tabela" por linha no arquivo "tabela_csv"