#
# 1.	 Construa uma calculadora que seja uma classe. As operações que deve existir na
# calculara são: Somar, subtrair, multiplicar, dividir (não pode ter divisão por zero),
# potência, listar os últimos resultados.
#
class Calculadora: # classe calculadora

    def __init__(self): # inicializador
        self.resultado = 0 # atributo
        self.lista = [] # atributo

    def somar(self, num1, num2): # método de instância (método de classe)
        self.resultado = num1 + num2  # calcula o resultado da soma
        self.lista.append(self.resultado) # adiciona o resultado na lista de resultados
        return self.resultado  # retorna o resultado

    def subtrair(self, num1, num2): # método de instância (método de classe)
        self.resultado = num1 - num2  # calcula o resultado da subtração
        self.lista.append(self.resultado) # adiciona o resultado na lista de resultados
        return self.resultado # retorna o resultado

    def multiplicar(self, num1, num2):
        self.resultado = num1 * num2 # calcula o resultado da multiplicação
        self.lista.append(self.resultado) # adiciona o resultado na lista de resultados
        return self.resultado # retorna o resultado
    
    def dividir(self, num1, num2):
        if num2 == 0:
            return "Não é possível dividir por zero"
        else:
            self.resultado = num1 / num2
            self.lista.append(self.resultado)
            return self.resultado
    def potencia(self, num1, num2):
        self.resultado = num1 ** num2
        self.lista.append(self.resultado)
        return self.resultado
    def listarUltimosResultados(self):
        return self.lista