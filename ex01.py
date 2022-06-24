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
        return f"{num1} + {num2} = {self.resultado}"  # retorna o resultado

    def subtrair(self, num1, num2): # método de instância (método de classe)
        self.resultado = num1 - num2  # calcula o resultado da subtração
        self.lista.append(self.resultado) # adiciona o resultado na lista de resultados
        return f"{num1} - {num2} = {self.resultado}" # retorna o resultado

    def multiplicar(self, num1, num2):
        self.resultado = num1 * num2 # calcula o resultado da multiplicação
        self.lista.append(self.resultado) # adiciona o resultado na lista de resultados
        return f"{num1} * {num2} = {self.resultado}" # retorna o resultado

    def dividir(self, num1, num2):
        if num2 == 0: # se o segundo número for zero retorna erro
            return f"{num2} = 0, Não é possível dividir por zero" # retorna erro
        else: # se não for zero calcula o resultado
            self.resultado = num1 / num2 # calcula o resultado da divisão de num1 por num2
            self.lista.append(self.resultado) # adiciona o resultado na lista de resultados
            return f"{num1} / {num2} = {self.resultado}" # retorna o resultado

    def potencia(self, num1, num2):
        self.resultado = num1 ** num2 # calcula o resultado da potência de num1 elevado a num2
        self.lista.append(self.resultado) # adiciona o resultado na lista de resultados
        return f"{num1} ^ {num2} = {self.resultado}" # retorna o resultado (num1 elevado a num2)

    def listarUltimosResultados(self):
        return self.lista # retorna a lista de resultados