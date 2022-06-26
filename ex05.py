
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 26/06/2022
#

#
# 5.	Você foi contratado para atualizar o código fonte do jogo PacMan. Após analisar o jogo,
# você identificou que existem 5 classes no jogo (mapa, PacMan, fantasma, moedas e frutas que dão poderes ao PacMan)
# e mapeou os atributos e métodos de cada classe, começando a codificação a partir da classe do PacMan, logo,
# escreva os métodos e atributos destas classes.
#
# as classes abaixo são apenas uma ideia

class PacMan:
    def __init__(self, nome, energia, pontos, posicao): # Inicializador (método de classe)
        self.nome = nome
        self.energia = energia
        self.pontos = pontos
        self.posicao = posicao

    def andar(self): # Método de instância (método de classe)
        print("Andando...")

    def correr(self):
        print("Correndo...")

    def pular(self):
        print("Pulando...")

    def morrer(self):
        print("Morrendo...")

    def comer(self):
        print("Comendo...")


class Mapa:   # Classe Mapa
    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho

    def carregar(self):
        print("Carregando mapa...")

    def desenhar(self):
        print("Desenhando mapa...")

    def salvar(self):
        print("Salvando mapa...")

class Fantasma:
    def __init__(self, nome, energia, pontos, posicao):
        self.nome = nome
        self.energia = energia
        self.pontos = pontos
        self.posicao = posicao

    def andar(self):
        print("Andando...")

    def correr(self):
        print("Correndo...")

    def morrer(self):
        print("Morrendo...")

class Moeda:
    def __init__(self, nome, pontos, posicao):
        self.nome = nome
        self.pontos = pontos
        self.posicao = posicao

    def pegar(self):
        print("Pegando moeda...")

    def soltar(self):
        print("Soltando moeda...")



class Fruta:
    def __init__(self, nome, pontos, posicao):
        self.nome = nome
        self.pontos = pontos
        self.posicao = posicao

    def pegar(self):
        print("Pegando fruta...")

    def soltar(self):
        print("Soltando fruta...")
