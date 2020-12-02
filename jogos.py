import forca
import adivinhacao
print("************************************","########Escolha o seu jogo##########","************************************",sep="\n")

print("(1)forca (2) advinhacao")

jogo = int(input("qual o jogo ?\n\n"))

if(jogo ==1):
    print("JOGO FORCA")
    forca.jogar()
elif(jogo == 2):
    print("JOGO ADIVINHACAO")
    adivinhacao.jogar()