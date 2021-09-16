print("Cálculo de Fatorial")
num = int(input("Digite o Fatorial: "))
contador = 1
result = 1

while contador <= num:
    result = result * contador
    contador = contador + 1

print("O Fatorial de ", num, " é: ", result)
print("\nFim do Programa")