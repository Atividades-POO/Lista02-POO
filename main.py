#
# 1 - importe o arquivo ex01.py e crie uma instância da classe calculadora
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
print(calc.dividir(10, 0)) # imprime Erro: Não é possível dividir por zero


#
print("-" * 40)
print()
#####################################################


# 2 - importe o arquivo ex02.py e crie uma instância da classe numero
from ex02 import Numero  # importa a classe numero
# 2.1 - crie uma instância da classe numero
num = Numero(10, 20) # instancia a classe numero
# 2.2 - chame os métodos da classe numero
num.imprime() # imprime os dois números
num.imprimePares() # soma os dois números

#
print("-" * 20)
print()
#####################################################


# 3 - importe o arquivo ex03.py e crie uma instância da classe fatorial
from ex03 import Fatorial  # importa a classe fatorial
# 3.1 - crie uma instância da classe fatorial
f = Fatorial(5) # instancia a classe fatorial
# 3.2 - chame os métodos da classe fatorial
f.imprime() # imprime o fatorial de 5
f.fatorial() # imprime o fatorial de 5


#
print("-" * 20)
print()
#####################################################

# 4 - importe o arquivo ex04.py e crie uma instância da classe PessoaIMC
from ex04 import PessoaIMC  # importa a classe pessoaIMC
# 4.1 - crie uma instância da classe PessoaIMC
p1 = PessoaIMC("João", 80, 1.80) # instancia a classe pessoaIMC
p2 = PessoaIMC("Maria", 70, 1.60) # instancia a classe pessoaIMC
# 4.2 - chame os métodos da classe PessoaIMC
print(f'a situação do {p1.nome} é de {p1.resultIMC()}') # imprime o IMC de João
print(f'a situação do {p2.nome} é de {p2.resultIMC()}') # imprime o IMC de Maria



#
print("-" * 20)
print()
#####################################################




