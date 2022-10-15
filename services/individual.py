from random import random, randint


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

    def crossover(self, outro_individuo):
        """Determina o ponto de crossover"""

        # um número randômico (0 ou 1) vai multiplicar pelo tamanho
        # do cromossomo (round é para arredondar)
        corte = int(round(random() * len(self.cromossomo)))

        # o filho recebe parte do cromossomo (de 0 até corte) do outro indíviduo
        filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
        # o outro_individuo é o individuo2
        filho2 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]

        filhos = [Individuo(self.minimos, self.maximos, self.geracao + 1),
                  Individuo(self.minimos, self.maximos, self.geracao + 1)]

        # filho 1 e 2 na verdade está criando cromossomos
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2

        return filhos

    def mutacao(self, taxa_mutacao, minimos, maximos):
        """Determina a mutação dos cromossomos"""

        # print(f"Antes: {self.cromossomo}")

        for i in range(len(self.cromossomo)):
            if random() < taxa_mutacao:
                if (type(minimos[i]) == float) and (type(maximos[i]) == float):
                    self.cromossomo[i] = random.uniform(
                        minimos[i], maximos[i])  # instance
                else:
                    self.cromossomo[i] = randint(minimos[i], maximos[i])
        # print(f"Depois: {self.cromossomo}")

        return self

# o cromossomo (str) será o conjunto dos valores (escolhidos entre o min e o max)
# o individuo será o próprio cromossomo
