total_de_figurinhas = int(input("Digite o total de figurinhas: ")) 
numero_de_amigos = int(input("Digite o número de amigos: ")) 

figurinhas_amigo = total_de_figurinhas // (numero_de_amigos + 2) 
figurinhas_joao = 2 * figurinhas_amigo 

print(f"João recebeu {figurinhas_joao} figurinhas")