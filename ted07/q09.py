# Programa para desenhar padrões simples com caracteres

def desenhar_triangulo(n):
    print("Triângulo:")
    for i in range(1, n + 1):
        print("* " * i)

def desenhar_quadrado(n):
    print("Quadrado:")
    for i in range(n):
        print("* " * n)

def desenhar_losango(n):
    print("Losango:")
    for i in range(n):
        # Desenha a parte superior do losango
        print(" " * (n - i - 1) + "* " * (i + 1))
    for i in range(n - 1):
        # Desenha a parte inferior do losango
        print(" " * (i + 1) + "* " * (n - i - 1))

# Solicita o tipo de padrão e a dimensão
print("Escolha um padrão:")
print("1. Triângulo")
print("2. Quadrado")
print("3. Losango")

opcao = int(input("Digite o número da opção escolhida: "))
n = int(input("Digite o número de linhas/colunas: "))

if opcao == 1:
    desenhar_triangulo(n)
elif opcao == 2:
    desenhar_quadrado(n)
elif opcao == 3:
    desenhar_losango(n)
else:
    print("Opção inválida!")
