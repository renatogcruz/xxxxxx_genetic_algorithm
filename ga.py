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

        print(f"Antes: {self.cromossomo}")

        for i in range(len(self.cromossomo)):
            if random() < taxa_mutacao:
                if (type(minimos[i]) == float) and (type(maximos[i]) == float):
                    self.cromossomo[i] = random.uniform(
                        minimos[i], maximos[i])  # instance
                else:
                    self.cromossomo[i] = randint(minimos[i], maximos[i])
        print(f"Depois: {self.cromossomo}")

        return self

# o cromossomo (str) será o conjunto dos valores (escolhidos entre o min e o max)
# o individuo será o próprio cromossomo


class AlgoritmoGenetico():

    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = 0

    def inicializa_populacao(self, minimos, maximos):
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo(minimos, maximos))
        self.melhor_solucao = self.populacao[0]

    def ordena_populacao(self, objetivo='maximizar'):
        # AQUI DEVE ENTRAR SE É MINIMIZAÇÃO OU MAXIMIZAÇÃO (objetivo deverá ser um input)

        if objetivo == 'maximizar':
            reverse = True
        else:
            reverse = False

        self.populacao = sorted(self.populacao,
                                key=lambda populacao: populacao.nota_avaliacao,
                                reverse=reverse)

        # HÁ ALTERAÇÃO NOS VALORES, MAS AINDA NÃO ENTENDO SE ESTÁ BOM OU NÃO :/
        # AINDA A MELHOR SOLUÇÃO NÃO É O MENOR NÚMERO


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

    # print(nome)
    # print(minimo)
    # print(maximo)

    print("Individuo 1")
    individuo1 = Individuo(minimo, maximo)
    # print(f"Minimos {individuo1.minimos}")
    # print(f"Máximos {individuo1.maximos}")
    # print(f"Geração {individuo1.geracao}")
    # cromossomo aqui significa (altura, largura, comprimento)
    print(f"Cromossomo {individuo1.cromossomo}")

    individuo1.avaliacao()
    print(f"Nota: {individuo1.nota_avaliacao}\n")

    print("Individuo 2")
    individuo2 = Individuo(minimo, maximo)
    # cromossomo aqui significa (altura, largura, comprimento)
    print(f"Cromossomo {individuo2.cromossomo}")

    individuo2.avaliacao()
    print(f"Nota: {individuo2.nota_avaliacao}\n")

    # testando crossover
    individuo1.crossover(individuo2)

    # testando mutação
    individuo1.mutacao(0.5, minimo, maximo)
    individuo2.mutacao(0.5, minimo, maximo)
