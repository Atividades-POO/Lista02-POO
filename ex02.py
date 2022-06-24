#
# 2.	Construa uma classe que ao ser instanciada ela retorne os números pares entre dois valores,
# passados na inicialização, incluindo-os.
#
class Numero:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def imprime(self):
        print(f"valor1 = {self.num1}, valor2 = {self.num2}")   # imprime os dois números
    def imprimePares(self):
        for i in range(self.num1, self.num2+1):
            if i % 2 == 0:
                print(i)