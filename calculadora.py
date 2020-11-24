class Calculadora:

    def sumar(self, valor1, valor2):
        return valor1 + valor2

    def restar(self, valor1, valor2):
        return valor1 - valor2

    def multiplicar(self, valor1, valor2):
        return valor1 * valor2

    def dividir(self, valor1, valor2):
        if valor2==0:
            return "operationError"
        else:
            return valor1 / valor2

    def potenciar(self, valor1, valor2):
        return valor1 ** valor2

    def fatorial(self, valor):
        if valor < 0:
            return "operationError"
        elif valor == 0:
            return 1
        else:
            factorial = 1
            for i in range(1, valor + 1):
                factorial = factorial*i
            return factorial

#cal = Calculadora()
#print(cal.dividir(2, 10))
#print(cal.potenciar(100, -2))
#print(cal.potenciar(-5, -5))
#rint(cal.dividir(5, 0))
