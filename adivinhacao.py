import random as rd

def jogar():
    print("************************************","ola bem vido ao jogo de adivinhacao","************************************",sep="\n")
    numero_secreto = rd.randrange(1,101,1)
    total_de_tentativas = 3
    pontos = 1000
    print("digite um nível (1) facil (2) medio (3) dificil")
    nivel = int(input())

    if(nivel == 1):
        total_de_tentativas=20
    elif(nivel == 2):
        total_de_tentativas=10
    elif(nivel == 3):
        total_de_tentativas=5

    for rodada in range(1,total_de_tentativas + 1):
        print("digite um numero entre 1 a 100:",end="\n\n")
        print("tentativa {} de {}".format(rodada,total_de_tentativas))
        chute = int(input("digite o seu numero\n"))
        if(chute<1 or chute>100):
            print("numero invalido")
            continue
        print("voce digitou: ",chute)
        interator = 0
        acertou = chute == numero_secreto
        maior =   chute >  numero_secreto
        menor =   chute <  numero_secreto
        if(acertou):
            print("voce acertou e fez {} pontos".format(pontos))
            break
        else:

            print("voce errou")
            if(maior):
                print("seu chute foi maior")
            elif(menor):
                print("seu chute foi menor")
        pontos_perdidos = abs(numero_secreto-chute)
        pontos -= pontos_perdidos
    print("fim do jogo")
    print("o numero era {}".format(numero_secreto))
if(__name__ == "__main__"):
    jogar()