palavra = input("Digite uma palavra: ").lower()  # Converte a palavra para minúsculas
vogais = "aeiou"
contador = 0

for letra in palavra:
    if letra in vogais:
        contador += 1

print(f"A palavra '{palavra}' tem {contador} vogais.")
