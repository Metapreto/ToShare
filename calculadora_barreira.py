#    O código serve para calcular o raio de uma esfera fechada com sua barreira
# completa

# ENTRADAS
RAIO_BARREIRA_PESSOAL = 2.5

chave_de_retorno = True
while chave_de_retorno:  # início do loop

    raio = input(
        "DIGITE O VALOR DA AMPLIAÇÃO - EFEITO EM ÁREA- EM METROS: "
    )  # Solicita o raio do nível da ataque que está na ampliação efeito em área
    if raio.isdigit():  # Condição: verifica se o valor de raio é inteiro

        # VARIÁVEIS
        altura = float(raio)  # Medida fornecida pela vantagem Wall
        base = 3 * float(raio)  # Medida fornecida pela vantagem Wall
        area_retangulo = (
            base * altura
        )  # Calcula a área do retângulo descrito na ampliação Wall

        print(area_retangulo, "m")

        # CALCULOS
        raio_esfera = area_retangulo / (
            12.56
        )  # Mostra o raio da esfera resultante da Ampliação Wall.
        area_esfera_pessoal = 12.56 * RAIO_BARREIRA_PESSOAL
        espessura = area_retangulo / area_esfera_pessoal
        # SAÍDAS

        print(f"ESPESSURA MÁXIMA: {espessura}m\nRAIO MÍNIMO:{RAIO_BARREIRA_PESSOAL}m\n")
        print(f"ESPESSURA MINIMA: 1m\nRAIO MÁXIMO:{raio_esfera}m\n")
    else:

        print("")
        print(
            "Você não digitou um valor válido"
        )  # Mesagem mostrada caso o valor de Raio não seja inteiro
        print("")

    resposta = input(
        "Deseja calcular outro valor[s/n]: "
    ).lower()  # Pergunta para encerrar o loop
    print("")

    while resposta == "s" or "n":
        if resposta == "s":
            break
        elif resposta == "n":
            print("Fim de programa.")
            chave_de_retorno = False
            break
        else:
            resposta = input(
                "Desculpe, não entendi. Se deseja calcular outro valor, digite [s]"
                " Caso deseje sair, pressione [n]"
            )
