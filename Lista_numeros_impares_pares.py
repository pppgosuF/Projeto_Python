print("Sequência de números e separação de pares e ímpares: ")
n = int(input("Digite o numero final da contagem: "))
lista = []
lista_imp = []
lista_par = []

for i in range(0,n+1):
  lista.append(i)
  if i % 2 :
    i != 0
    lista_imp.append(i)
  else:
    lista_par.append(i)

print("Sequência Numérica: \n", lista,"\nLista de Números pares: \n", lista_par, "\nLista Números ímpares: \n", lista_imp)
print("\nFim do Programa")