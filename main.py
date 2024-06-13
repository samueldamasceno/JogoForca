# jogo da forca em python
import random

def bem_vindo():
    print("====== JOGO DA FORCA ======")
    print()
    print("Bem-vindo ao Jogo da Forca!")
    print()
    while True:
        print("""Você conhece as regras?
              1. Sim
              2. Não""")
        resposta = input("Digite a opção que deseja: ")
        if resposta == "1":
            print()
            print("Ótimo! Então vamos começar!")
            print()
            break
        elif resposta == "2":
            regras()
            break
        else:
            print()
            print("Opção inválida!")
            print()
            continue

def regras():
    print()
    print("Regras do jogo:")
    print()
    print("""O jogo irá escolher aleatoriamente uma palavra, e o seu objetivo é descobrí-la.
          Você pode chutar alguma letra que você acha que a palavra possui.
          Se você acertar a letra, ela aparecerá na palavra.
          Se você acertar todas as letras, você ganha!
          Se você acertar alguma letra que a palavra não possui, você perde uma vida!
          Você terá 5 vidas.
          Vamos lá?""")
    print()
    print("Boa sorte!")
    print()

def sortear_palavra():
    palavras = [
        "amarelo",
        "azul",
        "vermelho",
        "verde",
        "rosa",
        "laranja",
        "roxo",
        "preto",
        "branco",
        "cinza",
        "marrom",
    ]
    palavra_secreta = random.choice(palavras)
    return palavra_secreta

def jogo_forca():
    bem_vindo()
    palavra_secreta = sortear_palavra()
    print("JOGO DA FORCA")
    print()

    vidas = 5
    while vidas > 0:
        print(f"Você possui {vidas} vidas")
        print()

        for i in range(0, len(palavra_secreta)):
            print("_", end=" ")
        print()
        print("Digite uma letra ou chute a palavra")
        chute = input()
        if len(chute) > 1:
            if chute == palavra_secreta:
                print()
                print(f"Parabéns! A palavra secreta era {palavra_secreta}. Você acertou!")
                print()
                break
            else:
                print()
                print(f"Você errou! A palavra secreta não é {chute}")
                print()
                vidas -= 1
                continue
        elif len(chute) < 1:
            print()
            print("Digite uma letra ou chute a palavra")
            continue



jogo_forca()
