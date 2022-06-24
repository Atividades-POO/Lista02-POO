#
# 1 - impporte o arquivo ex01.py e crie uma instância da classe calculadora
from ex01 import Calculadora  # importa a classe calculadora
# 1.1 - crie uma instância da classe calculadora
calc = Calculadora() # instancia a classe calculadora
# 1.2 - chame os métodos da classe calculadora
calc.somar(10, 20) # vai somar 10 e 20 e vai imprimir 30
calc.subtrair(10, 20) # vai subtrair 20 de 10 e vai imprimir -10
calc.multiplicar(10, 20) # vai multiplicar 10 e 20 e vai imprimir 200
calc.dividir(10, 20) # vai dividir 10 por 20 e vai imprimir 0.5
calc.potencia(10, 2) # vai calcular a potência de 10 elevado a 2 e vai imprimir 100
# 1.3 - imprime uma lista dos últimos resultados da calculadora
print(calc.listarUltimosResultados()) # imprime a lista de resultados
# 1.4 - calcule uma multiplação e uma divisão
print(calc.multiplicar(10, 20) + calc.dividir(10, 20)) # imprime 200 + 0.5
print(calc.listarUltimosResultados()) # imprime a lista de resultados
# 1.5 - calcule uma potência e uma divisão por zero
print(calc.potencia(10, 2)) # imprime 100
print(calc.dividir(10, 0)) # imprime  Erro: Não é possível dividir por zero

