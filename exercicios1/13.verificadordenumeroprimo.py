numero = int(input("Digite um número:"))
primo = True

if numero < 2:
    primo = False

else:
    for i in range(2, numero):
        if numero % i == 0:
            primo = False


if primo:
    print("O número", numero, "é primo.")

else:
    print("O número", numero, "não é primo.")