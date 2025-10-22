# Código para calcular o fatorial de um número qualquer, feito em ProgComp[2025.1].
# Usado como base!
'''
fat = int(input("Digite um numero: ")) 
produto = 1
n = 1
while n <= fat:
    produto = produto*n
    n = n + 1
print("O fatorial de",fat,"é",produto)
'''
# v1 Calcula para um número especifico!
'''
strnum = input("Digite um numero: ")
soma_fats = 0
for x in strnum:
    fat = int(x)
    #print(x)
    produto = 1
    n = 1
    while n <= fat:
        produto = produto*n
        n = n + 1
        #print(n,"N")
    soma_fats += produto
#print(soma_fats)
if soma_fats == int(strnum):
    print("EQUIVALENTES",strnum,soma_fats)
else: print("DIFERENTES",strnum,soma_fats)
'''
# v2
for z in range(10,int(7*(str(9)))): # 7 * str(9) = 9999999
    #print(z)
    if int(z)%1000000 == 0: 
        print(z,int(z/100000),"%","de progresso")
    strnum = str(z)  #input("Digite um numero: ")
    soma_fats = 0
    for x in strnum:
        fat = int(x)
        #print(x)
        produto = 1
        n = 1
        while n <= fat:
            produto = produto*n
            n = n + 1
            #print(n,"N")
        soma_fats += produto
    #print(soma_fats)
    if soma_fats == int(strnum):
        print("EQUIVALENTES","Número:",strnum,"--> Soma dos fatoriais de cada algarismo:",soma_fats)
    #else: print("DIFERENTES",strnum,soma_fats)
print ("100",'%', "de progresso")
