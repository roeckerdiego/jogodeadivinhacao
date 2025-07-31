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