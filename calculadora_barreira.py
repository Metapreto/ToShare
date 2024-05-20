#    O código serve para calcular o raio de uma esfera fechada com sua barreira
# completa

# ENTRADAS
RAIO_BARREIRA_PESSOAL = 2.5

chave_de_retorno = True
while chave_de_retorno:  # início do loop

    raio = input(
        "\nDIGITE O VALOR DA AMPLIAÇÃO - EFEITO EM ÁREA- EM METROS: "
    )  # Solicita o raio do nível da ataque que está na ampliação efeito em área
    if raio.isdigit():  # Condição: verifica se o valor de raio é inteiro

        # VARIÁVEIS
        altura = float(raio)  # Medida fornecida pela vantagem Wall
        base = 3 * float(raio)  # Medida fornecida pela vantagem Wall
        area_retangulo = (
            base * altura
        )  # Calcula a área do retângulo descrito na ampliação Wall

        print("\nA área do retângulo é : ", area_retangulo, "m²")

        # CALCULOS
        raio_esfera = area_retangulo / (
            12.56
        )  # Mostra o raio da esfera resultante da Ampliação Wall.
        area_esfera_pessoal = 12.56 * RAIO_BARREIRA_PESSOAL
        espessura = area_retangulo / area_esfera_pessoal
        # SAÍDAS

        print(f"\nO raio da BARREIRA é {raio_esfera:.2f}m\n")
    else:

        print(
            "\nVocê não digitou um valor válido\n"
        )  # Mesagem mostrada caso o valor de Raio não seja inteiro

    resposta = input(
        "\nDeseja calcular outro valor[s/n]:\n "
    ).lower()  # Pergunta para encerrar o loop

    while resposta == "s" or "n":
        if resposta == "s":
            break
        elif resposta == "n":
            print("\nFim de programa.\n")
            chave_de_retorno = False
            break
        else:
            resposta = input(
                "\nDesculpe, não entendi. Se deseja calcular outro valor, digite [s]"
                " Caso deseje sair, pressione [n]\n"
            )
