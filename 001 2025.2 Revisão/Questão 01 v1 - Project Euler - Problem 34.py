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