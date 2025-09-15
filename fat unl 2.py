#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      20251014050003
#
# Created:     15/09/2025
# Copyright:   (c) 20251014050003 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
'''
fat = int(input("Digite um numero: "))
produto = 1
n = 1
while n <= fat:
    produto = produto*n
    n = n + 1
print("O fatorial de",fat,"é",produto)
'''
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
'''
for z in range(1,1000000000001):
    #print(z)
    if int(z)%10000000 == 0: 
        print(z,"Progresso")
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
        print("EQUIVALENTES",soma_fats)