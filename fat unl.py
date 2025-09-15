
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
    print("EQUIVALENTES")