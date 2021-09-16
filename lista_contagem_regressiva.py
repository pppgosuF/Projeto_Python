num = int(input("Digite o numero para contagem regressiva: "))
lista = []
for i in range(0,num+1):
  lista.append(i)
lista.reverse()

for item in lista:
    print("Contagem em ", item )

print("\nFim do Programa")