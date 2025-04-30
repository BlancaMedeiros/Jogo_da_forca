import random
import os

palavra_secreta = ["abacaxi", "amor", "bicicleta", "cachorro", "futebol", "jardim", "carro", "sol", "lua", "chocolate",
    "computador", "telefone", "girassol", "arco", "avião", "bola", "gato", "elefante", "flor", "janela",
    "sorvete", "travesseiro", "banana", "relógio", "guitarra", "banco", "cachoeira", "orquestra", "piano",
    "televisao", "pintura", "arte", "tigre", "pedra", "piscina", "escola", "sombra", "café", "caminhao",
    "lixeira", "teclado", "computacao", "guerra", "dente", "cabelos", "livro", "sucesso", "festa", "fumaça",
    "espada", "parque", "geladeira", "martelo", "relacionamento", "rato", "pato", "foca", "macaco", "morcego",
    "onibus", "camisa", "botas", "roupas", "navio", "dinheiro", "poder", "batata", "praia", "nuvem", "balanco",
    "mercado", "livros", "areia", "lagarto", "fotografia", "deserto", "floresta", "planeta", "futuro", "sonho",
    "pintor", "roda", "espelho", "poesia", "fantasma", "arroz", "aventureiro", "melancia", "quadro", "anjo",
    "satélite", "giraffe", "terremoto", "vampiro", "música", "cantor", "corpo", "pessoa", "ilha", "salada",
    "animal", "azul", "branco", "verde", "travesseiro", "planalto", "fluminense", "estadio", "cachorrinho",
    "conhecimento", "telefone", "amizade", "paz", "desafio", "mirante", "flamengo", "sorvete", "perigo", "guerreiro",
    "palmeiras", "mergulhador", "universo", "coração", "realidade", "exploração", "suspense", "inovação", "garra",
    "iluminado", "inverno", "temperatura", "avivamento", "preparativo", "presente", "vida", "sabedoria", "sabores",
    "luz", "exemplo", "escrita", "batalha", "silêncio", "cozinha", "estrela", "mágica", "alegria", "prazer", "extremo"]

palavra_sorteada = random.choice(palavra_secreta)
tracinhos = ["_"] * len(palavra_sorteada)
tentativas = 6
letras_erradas = []

while True:
    os.system('cls')
    print(f"Você ainda tem {tentativas} tentativas")
    print(''.join(tracinhos))
    print("Essas letras não existem na palavra: ", letras_erradas)
    letras = input("Digite uma letra: ")
    acertou = False

    for i, letra in enumerate(palavra_sorteada):
        if letras == letra:
            tracinhos[i] = letras
            acertou = True

    if acertou:
        if not "_" in tracinhos:
            print("Você ganhou o jogo!")
            break
    else:
        letras_erradas.append(letras)
        tentativas = tentativas - 1

        if tentativas == 0:
            print("Game Over")
            break

    

