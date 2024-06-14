# jogo da forca em python
import random
import palavras
import os

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
    print("""Escolha um tema para o nosso jogo começar: 
          1. Cores
          2. Frutas
          3. Nomes
          4. Animais
          5. Países""")

    while True:
        tema = input("Digite a opção que deseja: ")
        if tema == "1":
            palavra_secreta = random.choice(palavras.cores)
            break
        elif tema == "2":
            palavra_secreta = random.choice(palavras.frutas)
            break
        elif tema == "3":
            palavra_secreta = random.choice(palavras.nomes)
            break
        elif tema == "4":
            palavra_secreta = random.choice(palavras.animais)
            break
        elif tema == "5":
            palavra_secreta = random.choice(palavras.paises)
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")
            digite_enter()

    return palavra_secreta

def mostrar_palavra(letras_palavra):
    print("Palavra secreta: ", end="")
    for letra in letras_palavra:
        print(letra, end=" ")
    print()

def mostrar_letras_erradas(letras_erradas):
    if len(letras_erradas) > 0:
        print("Letras erradas: ", end="")
        for letra in letras_erradas:
            print(letra, end=" ")
        print()

def vitoria(palavra):
    print()
    print(f"Parabéns! A palavra secreta era '{palavra}'. Você acertou!")
    print()

def derrota(palavra):
    print()
    print(f"Você perdeu! A palavra secreta era '{palavra}'.")
    print()

def digite_enter():
    input("Digite ENTER para continuar")

def jogo_forca():
    os.system('cls' if os.name == 'nt' else 'clear')
    bem_vindo()

    print("JOGO DA FORCA")
    print()

    vidas = 5

    palavra_secreta = sortear_palavra()
    letras_palavra = ["_"] * len(palavra_secreta)
    letras_erradas = []

    while vidas > 0:
        print(f"Você possui {vidas} vidas")
        
        mostrar_palavra(letras_palavra)
        mostrar_letras_erradas(letras_erradas)
    
        print("Digite uma letra ou chute a palavra:")
        chute = input()

        if len(chute) == 1:
            chute = chute.lower()

            if chute in letras_palavra or chute in letras_erradas:
                print("Você já chutou essa letra.")
                digite_enter()
                continue

            acertou = False
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i].lower() == chute:
                    letras_palavra[i] = palavra_secreta[i]
                    acertou = True

            if acertou:
                if "_" not in letras_palavra:
                    vitoria(palavra_secreta)
                    digite_enter()
                    break
            else:
                letras_erradas.append(chute)
                vidas -= 1
                print(f"A palavra secreta não tem a letra '{chute}'")

        elif len(chute) > 1:
            if chute.lower() == palavra_secreta.lower():
                vitoria(palavra_secreta)
                digite_enter()
                break
            else:
                vidas -= 1
                print(f"Você errou! A palavra secreta não é '{chute}'")
        
        print()

    if vidas == 0:
        derrota(palavra_secreta)
        digite_enter()

while True:
    jogo_forca()
    print()
    while True:
        print("""Deseja jogar novamente?
            1. Sim
            2. Não""")
        opcao = input()
        if opcao == "1":
            print()
            break
        elif opcao == "2":
            print("Obrigado por ter jogado!")
            exit()
        else:
            print()
            print("Opção inválida!")
            print()
            continue
