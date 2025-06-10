aliquota = 0.11 # 11%

# Entrada de dados
print("-------- Tabela Vigente (2023) ----------")
nome = input("Olá, digite seu nome: ")
print(f"Prazer {nome}, vamos começar.")

salario = float(input("Digite o seu salario: R$ "))

# Cálculo do desconto
desconto = salario * aliquota
salario_descontado = salario - desconto

# Saída formatada
print("-" * 40)
print(f"\033[0;33;46mSeu desconto no INSS é de R${desconto:.2f}]")
print(f"{nome}, seu salário com desconto é de R${salario_descontado:.2f}")
print("-" * 40)