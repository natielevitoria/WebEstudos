N = int(input("Digite um número N: "))

soma = 0
for i in range(1, N + 1):
    soma += i

print(f"A soma de todos os números de 1 até {N} é {soma}.")
