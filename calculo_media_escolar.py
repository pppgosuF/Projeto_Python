print ("Cálculo de Média")
nota_1 = int(input("Digite a primeira nota: "))
while nota_1 > 10:
  print("Nota não pode ser maior que 10!!")
  nota_1 = int(input("Digite a nota novamente: "))

nota_2 = int(input("Digite a segunda nota: "))
while nota_2 > 10:
  print("Nota não pode ser maior que 10!!")
  nota_2 = int(input("Digite a nota novamente: "))
    
nota_3 = int(input("Digite a terceira nota: "))
while nota_3 > 10:
  print("Nota não pode ser maior que 10!!")
  nota_3 = int(input("Digite a nota novamente: "))
    
nota_4 = int(input("Digite a quarta nota: "))
while nota_4 > 10:
  print("Nota não pode ser maior que 10!!")
  nota_4 = int(input("Digite a nota novamente: "))
    
lista_nota = [nota_1,nota_2,nota_3,nota_4]
media = (nota_1 + nota_2 + nota_3 + nota_4)/4

for item in lista_nota:
    print("Notas: ", item)
    
if media >= 6:
  print("Parabéns você foi Aprovado :) !!!\nMédia: ", media)
else:
    print("Infelizmente precisa de recuperação :( !!!\nMédia: ", media)
    
print("\nFim do Programa")