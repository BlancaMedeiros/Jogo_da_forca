import random
import os

palavra_secreta = ["abacaxi", "amor", "bicicleta", "cachorro", "futebol", "jardim", "carro", "sol", "lua", "chocolate",
    "computador", "telefone", "girassol", "arco", "aviao", "avião", "bola", "gato", "elefante", "flor",
    "janela", "sorvete", "travesseiro", "banana", "relógio", "guitarra", "banco", "cachoeira", "orquestra",
    "piano", "televisao", "pintura", "arte", "tigre", "pedra", "piscina", "escola", "sombra", "café",
    "caminhao", "lixeira", "relógio", "teclado", "computacao", "amor", "guerra", "dente", "cabelos", "livro",
    "sucesso", "piano", "festa", "guerra", "fumaça", "espada", "parque", "geladeira", "martelo", "carro",
    "relacionamento", "rato", "pato", "foca", "bicicleta", "cachorrinho", "gato", "macaco", "morcego",
    "tigre", "onibus", "camisa", "botas", "telefone", "roupas", "navio", "dinheiro", "poder", "tigre",
    "batata", "bola", "praia", "nuvem", "sol", "balanco", "mercado", "livros", "areia", "lagarto",
    "fotografia", "deserto", "floresta", "planeta", "sol", "lua", "futuro", "sonho", "pintor", "roda",
    "espelho", "poesia", "fantasma", "elefante", "arroz", "aventureiro", "mercado", "melancia", "quadro",
    "anjo", "satélite", "giraffe", "terremoto", "piano", "vampiro", "música", "cantor", "banco", "corpo",
    "pessoa", "ilha", "salada", "animal", "azul", "branco", "verde", "travesseiro"]
palavra_sorteada = random.choice(palavra_secreta)
os.system('cls')
tracinhos = "_" * len(palavra_sorteada)
print(tracinhos)