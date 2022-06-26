#
# Autores:
# michel silva
#
#
# data: 26/06/2022
#
# 3.	construa uma classe que ao ser instanciada ela retorne o valor fatorial de um número
# passado na sua inicialização.
#
class Fatorial: # classe que retorna o valor fatorial de um número passado na sua inicialização

    def __init__(self, num): # inicializador (método de classe)
        self.num = num   # atributo (método de instância)

    def imprime(self): # método de instância (método de classe)
        print(f"valor = {self.num}")  # imprime o número

    def fatorial(self): # método de instância (método de classe)
        fatorial = 1 # inicializa o fatorial com 1
        for i in range(1, self.num+1): # percorre o intervalo de números passados na inicialização
            fatorial = fatorial * i # multiplica o fatorial pelo número atual do loop e atualiza o fatorial
        print(f"fatorial = {fatorial}") # imprime o fatorial