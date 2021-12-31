from random import random, randint


class Parametro():
    """No Grasshopper, todo paamêtro tem 1 nome e 
    um valor que vai de um min até um max."""

    def __init__(self, nome, minimo, maximo):  # o valor entra nesse algoritmo
        self.nome = nome  # parametro nome. Ex.: largura
        self.minimo = minimo  # parametro min. Ex.: 1
        self.maximo = maximo  # parametro max. Ex.: 10


# class Individuo():
#     """Definição"""

#     def __init__(self, minimos, maximos, geracao=0):
#         self.minimos = minimos
#         self.maximos = maximos
#         self.nota_avaliacao = 0
#         self.geracao = geracao
#         self.cromossomo = []  # valores entre min e max dos parametros

#         # escolher valores entre min e max aleatoriamente
#         for i in range(len(lista_parametros)):
#             if (type(minimos[i]) == float) and (type(maximos[i]) == float):
#                 self.cromossomo.append(random.uniform(
#                     minimos[i], maximos[i]))  # instance
#             else:
#                 self.cromossomo.append(randint(minimos[i], maximos[i]))


# o cromossomo (str) será o conjunto dos valores (escolhidos entre o min e o max)
# o individuo será o próprio cromossomo

if __name__ == '__main__':
    # params1 = Parametro('altura', 0, 10)
    lista_parametros = []
    lista_parametros.append(Parametro('altura', 2, 10))
    lista_parametros.append(Parametro('largura', 5, 10))
    lista_parametros.append(Parametro('comprimento', 2, 20))

    for parametro in lista_parametros:
        print(parametro.nome)
