print("---------------------------------")
print("Bem vindo ao jogo de adivinhação!")
print("---------------------------------")

numero_secreto=42

chute = input("Digite o seu número: \n")
chute_2 = int(chute)

if (numero_secreto == chute_2): 
    print("Você acertou!\n")
else:
    print("Voce errou")