import random

numero_secreto = random.randint(1, 10)
tentativa = int(input("Adivinhe o número entre 1 e 10: "))

if tentativa == numero_secreto:
    print("Parabéns! Você acertou o número!")
else:
    print(f"Errou! O número era {numero_secreto}. Tente de novo!")