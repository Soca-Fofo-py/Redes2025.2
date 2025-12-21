import os

diretorio = ".\\MeuEscopo\\"
var = "..\\test.txt"
abs = diretorio + var
#abs = var

real = os.path.realpath(abs)
absoluto = os.path.abspath(abs)
print("dire: ",os.path.realpath(diretorio))
print(abs)
print("Real: ",real)
print("Abso: ",absoluto)

if absoluto.startswith(os.path.realpath(diretorio)):
    print("Válido.")
