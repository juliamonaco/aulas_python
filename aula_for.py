print("---------------------------------")
print("Bem vindo ao jogo de adivinhação!")
print("---------------------------------")

numero_secreto=42
total_tentativas = 10


for rodada in range(1, total_tentativas + 1):
    print("Tentativa {} de {}" .format(rodada, total_tentativas, "\n"))
    chute = input("Digite o seu número: ")
    print("--------------------------------------------------")
    print("Você digitou", chute)
    chute_2 = int(chute)
    
    print("--------------------------------------------------")



    acertou = chute_2 == numero_secreto
    menor = chute_2 < numero_secreto
    maior = chute_2 > numero_secreto



    if (acertou): 
        print("Você acertou!\n \n")
    else:
        if(maior):
            print("Voce errou, seu chute foi maior que o numero secreto")
        elif(menor):
            print("Voce errou, seu chute foi menor que o numero secreto")
    
    print("-------------------------------------------------- \n")
        
    rodada = rodada + 1
   

print("-----------")    
print("Fim do jogo!")
print("-----------")