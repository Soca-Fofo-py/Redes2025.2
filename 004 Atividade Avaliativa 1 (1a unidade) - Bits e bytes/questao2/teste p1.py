def funcao_chamada():
  print("Esta é a função chamada.")

def funcao_chamadora():
  print("Esta é a função chamadora.")
  funcao_chamada() # Aqui a funcao_chamada é chamada
  print("Chamada concluída.")

# Para iniciar, chamamos a função externa
funcao_chamadora()
