from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/")
def index():

    return "Hello, GA"


@app.route("/run")
def run():

    lista_parametros = []

    lista_parametros.append(Parametro('altura', 2, 10))
    lista_parametros.append(Parametro('largura', 5, 10))
    lista_parametros.append(Parametro('comprimento', 2, 20))
    lista_parametros.append(Parametro('perfilA', 10, 1000))
    lista_parametros.append(Parametro('perfilB', 2, 5000))

    nome = []
    minimo = []
    maximo = []

    for parametro in lista_parametros:
        nome.append(parametro.nome)
        minimo.append(parametro.minimo)
        maximo.append(parametro.maximo)

    tamanho_populacao = 20
    objetivo = 'maximizar'
    taxa_mutacao = 0.05
    numero_geracoes = 100

    ag = AlgoritmoGenetico(tamanho_populacao, objetivo)

    # False é para cuspir os inputs no Grasshopper
    # True é para efetivamente executar o GA
    run = True

    resultado = ag.resolver(taxa_mutacao, numero_geracoes, minimo, maximo, run)

    # #################################### #
    # ag.inicializa_populacao(minimo, maximo)
    # # preenche as notas para cada individuo
    # for individuo in ag.populacao:
    #     individuo.avaliacao()
    # # ordena a lista pela nota
    # ag.ordena_populacao()
    # # monstra qual o melhor individuo
    # ag.melhor_individuo(ag.populacao[0])
    # for i in range(ag.tamanho_populacao):
    #     print(f"\n******* Individuo {i} *******",
    #           "\nCromossomo %s" % str(ag.populacao[i].cromossomo),
    #           "\nNota %s" % ag.populacao[i].nota_avaliacao)

    # # print(f"\nMelhor solução: %s" % ag.melhor_solucao.cromossomo,
    # #       "Melhor nota: %s" % ag.melhor_solucao.nota_avaliacao)

    # soma = ag.soma_avaliacoes()
    # print(f"Soma das avaliações: {soma}")

    # nova_populacao = []
    # probabilidade_mutacao = 0.05

    # for individuos_gerados in range(0, ag.tamanho_populacao, 2):
    #     pai1 = ag.seleciona_pai(soma)  # individuos_gerados
    #     pai2 = ag.seleciona_pai(soma)

    #     # filhos recebe uma lista de novos individuos
    #     filhos = ag.populacao[pai1].crossover(ag.populacao[pai2])
    #     nova_populacao.append(filhos[0].mutacao(
    #         probabilidade_mutacao, minimo, maximo))
    #     nova_populacao.append(filhos[1].mutacao(
    #         probabilidade_mutacao, minimo, maximo))

    # ag.populacao = list(nova_populacao)
    # # print(f"Pai 1: {pai1} | Pai 2 {pai2}")

    # for individuo in ag.populacao:
    #     individuo.avaliacao()
    # ag.ordena_populacao()
    # ag.melhor_individuo(ag.populacao[0])
    # soma = ag.soma_avaliacoes()

    # print(f"\nMelhor solução: %s" % ag.melhor_solucao.cromossomo,
    #       "Melhor nota: %s" % ag.melhor_solucao.nota_avaliacao)

    return jsonify(dict(status='success')), 200


@app.route('/route')
def route():

    if 'algo' == 'algo':

        return jsonify(dict(status='success')), 200
    else:
        return jsonify(dict(status='not relevant step')), 500


if __name__ == "__main__":
    app.run(debug=True)
