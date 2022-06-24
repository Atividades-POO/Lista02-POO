#
# 4.	Escreva (em python) uma classe PessoaIMC que contenha os atributos peso e altura, ambos do tipo float.
# Crie os métodos de acesso para estes atributos. Crie o método calculaIMC() que retorna um valor do tipo float
# correspondente ao IMC (Índice de Massa Corporal = peso / altura ao quadrado) calculado. Implemente também o método
# resultIMC() que retorna uma String com as seguintes informações:
# a.	Nome: <nome da pessoa>
# b.	Peso: <seu peso>
# c.	Altura: <sua altura>
# método de classe
# d.	Situação: <
# – 16,00 a 16,99 - Baixo peso Grau II
# – 17,00 a 18.49 - Baixo peso Grau I
# – 18,50 a 24,99 - Peso ideal
# – 25,00 a 29,99 - Sobrepeso
# – 30,00 a 34,99 - Obesidade Grau I
# – 35,00 a 39,99 - Obesidade Grau II >

class PessoaIMC:  # Classe PessoaIMC que contém os atributos peso e altura, ambos do tipo float
    def __init__(self, nome, peso, altura): # Inicializador (método de classe)
        self.nome = nome  # Atributo (método de instância)
        self.peso = float(peso)
        self.altura = float(altura)

    def calculaIMC(self): # Método de instância
        imc = self.peso / (self.altura ** 2) # Calcula o IMC (Índice de Massa Corporal = peso / altura ao quadrado)
        return imc # Retorna o valor do IMC calculado

    def resultIMC(self): # Método de instância
        if self.calculaIMC() < 16.00: # Se o IMC for menor que 16.00 (Baixo peso Grau II)
            return "Baixo peso Grau II" # Retorna "Baixo peso Grau II" (Situação)
        elif self.calculaIMC() >= 16.00 and self.calculaIMC() < 17.00: # Se o IMC for maior ou igual a 16.00 e menor que 17.00 (Baixo peso Grau I)
            return "Baixo peso Grau I"
        elif self.calculaIMC() >= 17.00 and self.calculaIMC() < 25.00: # Se o IMC for maior ou igual a 17.00 e menor que 25.00 (Peso ideal)
            return "Peso ideal"
        elif self.calculaIMC() >= 25.00 and self.calculaIMC() < 30.00: # Se o IMC for maior ou igual a 25.00 e menor que 30.00 (Sobrepeso)
            return "Sobrepeso"
        elif self.calculaIMC() >= 30.00 and self.calculaIMC() < 35.00: # Se o IMC for maior ou igual a 30.00 e menor que 35.00 (Obesidade Grau I)
            return "Obesidade Grau I"
        elif self.calculaIMC() >= 35.00 and self.calculaIMC() < 40.00: # Se o IMC for maior ou igual a 35.00 e menor que 40.00 (Obesidade Grau II)
            return "Obesidade Grau II" # Retorna "Obesidade Grau II" (Situação)
        elif self.calculaIMC() >= 40.00: # Se o IMC for maior ou igual a 40.00 (Obesidade Grau III)
            return "Obesidade Grau III" # Retorna "Obesidade Grau III" (Situação)