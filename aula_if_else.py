print("---------------------------------")
print("Bem vindo ao jogo de adivinhação!")
print("---------------------------------")

numero_secreto=42

chute = input("Digite o seu número: \n \n")

print("Você digitou\n", chute)
chute_2 = int(chute)

acertou = chute_2 == numero_secreto
menor = chute_2 < numero_secreto
maior = chute_2 > numero_secreto

if (acertou): 
    print("Você acertou!\n \n")
else:
    if(maior):
        print("Voce errou, seu chute foi maior que o numero secreto \n")
    elif(menor):
        print("Voce errou, seu chute foi menor que o numero secreto\n")
   

print("-----------")    
print("Fim do jogo")
print("-----------")