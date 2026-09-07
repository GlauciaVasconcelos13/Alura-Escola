dicionario = "qwertyuiopasdfghjklzxcvbnm"
alfabeto = "abcdefghijklmnopqrstuvwxyz"

def codifica(senha):
    senha_criptografada = ""
    for letra in senha:
        if "a" <= letra <= "z":
            posicao = ord(letra) - ord("a") # 0 até 25
            senha_criptografada += dicionario[posicao]
        else:
            senha_criptografada += letra
    return senha_criptografada