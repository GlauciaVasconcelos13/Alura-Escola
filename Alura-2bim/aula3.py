senha = "olecram"

def calcula_hash(senha):
    valor = 0
    for letra in senha:
        valor += ord(letra)
    return valor

print(calcula_hash("marcelo123"))