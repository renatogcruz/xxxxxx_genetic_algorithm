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

    def __init__(self, tamanho_populacao, objetivo):
        self.tamanho_populacao = tamanho_populacao
        self.objetivo = objetivo
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = 0

    def inicializa_populacao(self, minimos, maximos):
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo(minimos, maximos))
        self.melhor_solucao = self.populacao[0]

    def ordena_populacao(self):
        # AQUI DEVE ENTRAR SE É MINIMIZAÇÃO OU MAXIMIZAÇÃO (objetivo deverá ser um input)

        if self.objetivo == 'maximizar':
            reverse = True
        else:
            reverse = False
        self.populacao = sorted(self.populacao,
                                key=lambda populacao: populacao.nota_avaliacao,
                                reverse=reverse)

    def melhor_individuo(self, individuo):

        if self.objetivo == 'maximizar':
            if individuo.nota_avaliacao > self.melhor_solucao.nota_avaliacao:
                self.melhor_solucao = individuo
        else:
            if individuo.nota_avaliacao < self.melhor_solucao.nota_avaliacao:
                self.melhor_solucao = individuo

    def soma_avaliacoes(self):
        '''xxxx'''

        soma = 0
        for individuo in self.populacao:
            soma += individuo.nota_avaliacao

        return soma

    def seleciona_pai(self, soma_avaliacao):
        """Seleção dos indivíduos - método Roleta Viciada.
        Testar outras formas melhores de selecionar os pais"""

        pai = -1
        valor_sorteado = random() * soma_avaliacao
        soma = 0
        i = 0
        while i < len(self.populacao) and soma < valor_sorteado:
            soma += self.populacao[i].nota_avaliacao
            pai += 1
            i += 1

        return pai


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

    tamanho_populacao = 20
    objetivo = 'maximizar'

    ag = AlgoritmoGenetico(tamanho_populacao, objetivo)
    ag.inicializa_populacao(minimo, maximo)
    # preenche as notas para cada individuo
    for individuo in ag.populacao:
        individuo.avaliacao()
    # ordena a lista pela nota
    ag.ordena_populacao()
    # monstra qual o melhor individuo
    ag.melhor_individuo(ag.populacao[0])
    for i in range(ag.tamanho_populacao):
        print(f"\n******* Individuo {i} *******",
              "\nCromossomo %s" % str(ag.populacao[i].cromossomo),
              "\nNota %s" % ag.populacao[i].nota_avaliacao)

    print(f"\nMelhor solução: %s" % ag.melhor_solucao.cromossomo,
          "Melhor nota: %s" % ag.melhor_solucao.nota_avaliacao)

    soma = ag.soma_avaliacoes()
    print(f"Soma das avaliações: {soma}")

    for individuos_gerados in range(0, ag.tamanho_populacao, 2):
        pai1 = ag.seleciona_pai(soma)  # individuos_gerados
        # print(f"Pai 1: {pai1}")
        pai2 = ag.seleciona_pai(soma)
        # print(f"Pai 2: {pai1}")
    print(f"Pai 1: {pai1} | Pai 2 {pai2}")
