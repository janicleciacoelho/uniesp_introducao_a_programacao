import random

# O computador escolhe um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

# Inicializando variáveis
tentativas = 0
adivinhado = False

print("Tente adivinhar o número que estou pensando! (Entre 1 e 100)")

# Loop para tentativas do usuário
while not adivinhado:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    # Verifica se o palpite está correto
    if palpite == numero_secreto:
        adivinhado = True
        print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
    elif palpite < numero_secreto:
        print("O número é maior.")
    else:
        print("O número é menor.")
