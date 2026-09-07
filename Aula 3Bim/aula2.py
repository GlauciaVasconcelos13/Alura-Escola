def calcula_idade_maior(idade_monica, idade_filho1, idade_filho2): 
    idade_filho3 = idade_monica - idade_filho1 - idade_filho2 
    idade_maxima = max(idade_filho1, idade_filho2, idade_filho3) 
    return idade_filho3, idade_maxima

resultado = calcula_idade_maior(68, 12, 30) 
print(resultado)