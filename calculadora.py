class Soma:
    def calcular(self, a, b):
        return a + b

class Subtracao:
    def calcular(self, a, b):
        return a - b

class Multiplicacao:
    def calcular(self, a, b):
        return a * b

class Divisao:
    def calcular(self, a, b):
        if b == 0:
            return "Erro: Divisão por zero"
        return a / b

class RestoDivisao:
    def calcular(self, a, b):
        if b == 0:
            return "Erro: Divisão por zero"
        return a % b

soma = Soma()
subtracao = Subtracao()
multiplicacao = Multiplicacao()
divisao = Divisao()
resto_divisao = RestoDivisao()

print("Soma: ", soma.calcular(10, 5))
print("Subtração: ", subtracao.calcular(10, 5))
print("Multiplicação: ", multiplicacao.calcular(10, 5))
print("Divisão: ", divisao.calcular(10, 5))
print("Resto da Divisão: ", resto_divisao.calcular(10, 5))