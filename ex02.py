#
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 26/06/2022
#
#
# data: 26/06/2022
#
# 2.	Construa uma classe que ao ser instanciada ela retorne os números pares entre dois valores,
# passados na inicialização, incluindo-os.
#
class Numero: # classe que retorna os números pares entre dois valores, passados na inicialização, incluindo-os
    def __init__(self, num1, num2): # inicializador (método de classe)
        self.num1 = num1    # atributo (método de instância)
        self.num2 = num2

    def imprime(self): # método de instância (método de classe)
        print(f"valor1 = {self.num1}, valor2 = {self.num2}")   # imprime os dois números

    def imprimePares(self): # método de instância (método de classe)
        for i in range(self.num1, self.num2+1): # percorre o intervalo de números passados na inicialização
            if i % 2 == 0: # se o número for par imprime-o
                print(i) # imprime o número