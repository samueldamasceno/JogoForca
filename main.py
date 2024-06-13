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
    print("""O jogo irá escolher aleatoriamente uma palavra, e o seu objetivo é descobri-la.
          Você pode chutar alguma letra que você acha que a palavra possui.
          Se você acertar a letra, ela aparecerá na palavra.
          Se você acertar todas as letras, você ganha!
          Se você chutar alguma letra que a palavra não possui, você perde uma vida!
          Você também pode chutar uma palavra que você acha ser a palavra secreta.
          Mas se você errar, você perde uma vida!
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

    letras_palavra = ["_"] * len(palavra_secreta)
    letras_erradas = []

    while vidas > 0:
        print(f"Você possui {vidas} vidas")
        
        print("Palavra secreta: ", end="")
        for letra in letras_palavra:
            print(letra, end=" ")
        print()

        if len(letras_erradas) > 0:
            print("Letras erradas: ", end="")
            for letra in letras_erradas:
                print(letra, end=" ")
            print()
    
        print("Digite uma letra ou chute a palavra:")
        chute = input().lower()

        if len(chute) == 1:
            if chute in letras_palavra or chute in letras_erradas:
                print("Você já chutou essa letra.")
                continue

            if chute in palavra_secreta:
                for i in range(len(palavra_secreta)):
                    if palavra_secreta[i] == chute:
                        letras_palavra[i] = chute
                if "_" not in letras_palavra:
                    print()
                    print(f"Parabéns! A palavra secreta era '{palavra_secreta}'. Você acertou!")
                    print()
                    break
            else:
                letras_erradas.append(chute)
                vidas -= 1
                print(f"A palavra secreta não tem a letra '{chute}'")

        elif len(chute) > 1:
            if chute == palavra_secreta:
                print()
                print(f"Parabéns! A palavra secreta era '{palavra_secreta}'. Você acertou!")
                print()
                break
            else:
                vidas -= 1
                print()
                print(f"Você errou! A palavra secreta não é '{chute}'")
        
        print()

    if vidas == 0:
        print(f"Você perdeu! A palavra secreta era '{palavra_secreta}'.")

jogo_forca()
