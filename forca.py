import random as rd

def imprime_mensagem_abertura():
    print("************************************","ola bem vido ao jogo de forca!#####","************************************",sep="\n")

def carega_palavra_secreta():
    arquivo = open("palavras.txt")
    palavras = [palavra.strip().upper() for palavra in arquivo]
    palavra_secreta = palavras[rd.randrange(0, len(palavras))]
    arquivo.close()
    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letras in palavra_secreta]

def chute_do_jogador():
    chute_= input("Qual a letra\n")
    chute_ = chute_.strip().upper()
    return chute_

def imprime_mensagem_final(acertou,enforcou,palavra_secreta):
    print("fim de jogo")
    if(acertou):
       imprime_mensagem_vencedor()
    if(enforcou):
        imprime_mensagem_perdedor(palavra_secreta)

def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = chute_do_jogador()
        index = 0
        if (chute in palavra_secreta):
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
            print(letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)
            print("Ops, voce errou! Faltam {} tentativas".format(6 -erros))

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
    imprime_mensagem_final(acertou,enforcou,palavra_secreta)

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()