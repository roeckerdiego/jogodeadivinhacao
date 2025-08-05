import random 
print("🕶🕶🕶🕶🕶🕶🕶🕶🕶🕶🕶🕶🕶🕶🕶🕶🕶🕶🕶🕶🕶🕶🕶🕶🕶🕶")
print("                           ")
print("😃  Jogo de adivinhação  😃")
print("         criado por        ")
print("😍          diego        😍")
print("                           ")
print("🧐🧐🧐🧐🧐🧐🧐🧐🧐🧐🧐🧐🧐")

numeroSecreto = random.randrange(0,100)
totalTentativas = 0
pontos = 100

print("                               ")
print("Qual os níveis de dificuldade? ")
print("(1)- Fácil (2)- Médio (3)- Difícil ")

nivel = int(input("Escolha um nível: "))

if (nivel == 1):
    print("Você tem 20 tentativas. iiii ainda é um franguinho.")
    totalTentativas = 20
elif (nivel == 2):
    print("Você tem 10 tentativas. iiii ainda é um galizé.")
    totalTentativas = 10
elif (nivel == 3):
    print("Você tem 5 tentativas. iiii já é um galinho.")
    totalTentativas = 5
else:
    print("número inválido")

for rodada in range (1, totalTentativas +1):
    print("Tentativa {} de {}".format(rodada,totalTentativas) )
    chute_str = input("Digite um número entre 1 a 100: ")
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Número inválido")
        continue

    acertou = chute == numeroSecreto
    maior = chute > numeroSecreto
    menor = chute < numeroSecreto

    if(acertou):
        print(f"Você acertou e fez {pontos}! ")
        break
    else:
        if(maior):
            print("Você errou! seu chute foi maior que o número secreto")
        elif(menor):
            print("Você errou! seu chute foi menor que o número secreto")

            pontosPerdidos = abs(numeroSecreto - chute)
            pontos = pontos - pontosPerdidos

print("Fim de jogo! O número era ",numeroSecreto)