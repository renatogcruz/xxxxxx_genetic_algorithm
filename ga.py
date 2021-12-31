from random import random, randint


class Parametro():
    """No Grasshopper, todo paamêtro tem 1 nome e 
    um valor que vai de um min até um max."""

    def __init__(self, nome, minimo, maximo):  # o valor entra nesse algoritmo
        self.nome = nome  # parametro nome. Ex.: largura
        self.minimo = minimo  # parametro min. Ex.: 1
        self.maximo = maximo  # parametro max. Ex.: 10


class Individuo():
    """Definição"""

    def __init__(self, minimos, maximos, geracao=0):
        self.minimos = minimos
        self.maximos = maximos
        self.nota_avaliacao = 0
        self.geracao = geracao
        self.cromossomo = []  # valores entre min e max dos parametros

        # inicialização aleatória
        # escolher valores entre min e max aleatoriamente
        for i in range(len(lista_parametros)):
            if (type(minimos[i]) == float) and (type(maximos[i]) == float):
                self.cromossomo.append(random.uniform(
                    minimos[i], maximos[i]))  # instance
            else:
                self.cromossomo.append(randint(minimos[i], maximos[i]))

    def avaliacao(self):
        """Função fitness"""
        # Aqui deve receber o valor_objetivo de cada individuo (vem do modelo).
        # Por exemplo, relação área/volume.
        # função provisório para continuar o desenv. script
        nota = randint(1000, 2222)
        self.nota_avaliacao = nota


# o cromossomo (str) será o conjunto dos valores (escolhidos entre o min e o max)
# o individuo será o próprio cromossomo


if __name__ == '__main__':
    lista_parametros = []
    # params1 = Parametro('altura', 0, 10)
    lista_parametros.append(Parametro('altura', 2, 10))
    lista_parametros.append(Parametro('largura', 5, 10))
    lista_parametros.append(Parametro('comprimento', 2, 20))

    # for parametro in lista_parametros:
    #     print(parametro.nome)

    nome = []
    minimo = []
    maximo = []
    for parametro in lista_parametros:
        nome.append(parametro.nome)
        minimo.append(parametro.minimo)
        maximo.append(parametro.maximo)

    print(nome)
    print(minimo)
    print(maximo)

    individuo1 = Individuo(minimo, maximo)
    print(f"Minimos {individuo1.minimos}")
    print(f"Máximos {individuo1.maximos}")
    print(f"Geração {individuo1.geracao}")
    # cromossomo aqui significa (altura, largura, comprimento)
    print(f"Cromossomo {individuo1.cromossomo}")

    individuo1.avaliacao()
    print(f"Nota: {individuo1.nota_avaliacao}")
