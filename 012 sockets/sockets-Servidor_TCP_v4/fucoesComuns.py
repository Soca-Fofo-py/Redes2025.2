def f_dicio_to_json (diretorio):
    import os , json
    arquivos_a_oferecer = [f for f in os.listdir(diretorio) if os.path.isfile(os.path.join(diretorio, f))]
    #print(arquivos_a_oferecer)
    
    lista_arq_a_oferecer = []
    for n in arquivos_a_oferecer:
        nome_arq = diretorio + str(n)
        #print(nome_arq)
        tam_arq = os.path.getsize(nome_arq)
        lista_arq_a_oferecer.append({"nome":n,"Tamanho":tam_arq})
    #print(lista_arq_a_oferecer)
    listagem = json.dumps(lista_arq_a_oferecer)
    #print(listagem)

    tam_listagem = len(listagem)
    tam_listagem = tam_listagem.to_bytes(4,"big") # len da listagem
    #print(tam_listagem)
    return listagem , tam_listagem
    

diretorio = ".\\MeuEscopo\\"

lista , tamanho = f_dicio_to_json(diretorio)
print('Lista:',lista)
print('Tamanho da lista',tamanho)