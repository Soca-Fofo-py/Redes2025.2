def fdicio (diretorio):
    import os
    arquivos_a_oferecer = [f for f in os.listdir(diretorio) if os.path.isfile(os.path.join(diretorio, f))]
    print(arquivos_a_oferecer)
    a_o_f = ""
    for n in arquivos_a_oferecer:
        a_o_f += str(n) + " , "
    a_o_f = a_o_f[:len(a_o_f)-3].encode('utf-8') # Cria lista de arquivos a oferecer
    tam_listagem = len(a_o_f)
    tam_listagem = tam_listagem.to_bytes(4,"big") # len da lista
    print(a_o_f,tam_listagem)
    
    
diretorio = ".\\ofereco\\"
fdicio(diretorio)