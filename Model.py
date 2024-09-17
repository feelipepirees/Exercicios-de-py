class Model:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0


    def trocar(self, valorA, valorB):
        valorC = valorA
        valorA = valorB
        valorB = valorC
        return f'Valor A: {valorA} \nValor B: {valorB}'

    def tabuada(self, num):
        resultado = "" #Variavel String
        for i in range(0,11, 1):
            resultado += f'{num} * {i} = {num * i}\n'
        return resultado

    def media(self, nota1, nota2, nota3):
        return (nota1 + nota2 + nota3)/3
