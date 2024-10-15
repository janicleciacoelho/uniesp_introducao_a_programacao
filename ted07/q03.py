# Definindo as vogais
vogais = "aeiouAEIOU"

# Solicitando ao usuário uma frase
frase = input("Digite uma frase: ")

# Inicializando contadores
contador_vogais = 0
contador_consoantes = 0

# Percorrendo cada caractere da frase
for caractere in frase:
    # Verificando se é uma letra
    if caractere.isalpha():
        # Se for vogal, incrementa o contador de vogais
        if caractere in vogais:
            contador_vogais += 1
        else:
            # Se não for vogal, é consoante
            contador_consoantes += 1

# Exibindo o resultado
print(f"Total de vogais: {contador_vogais}")
print(f"Total de consoantes: {contador_consoantes}")
