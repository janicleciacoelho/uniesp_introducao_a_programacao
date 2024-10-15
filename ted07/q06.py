# Programa para verificar se um número é primo

num = int(input("Digite um número inteiro: "))

# Verifica se o número é menor que 2, pois 0 e 1 não são primos
if num < 2:
    print(f"{num} não é um número primo.")
else:
    # Variável para determinar se é primo
    primo = True
    
    # Verifica divisibilidade por números menores que ele (de 2 até num-1)
    for i in range(2, int(num ** 0.5) + 1):  # Testando até a raiz quadrada do número
        if num % i == 0:  # Se for divisível por i, não é primo
            primo = False
            break
    
    # Exibe o resultado
    if primo:
        print(f"{num} é um número primo.")
    else:
        print(f"{num} não é um número primo.")