import random

continuar_programa = True


while continuar_programa:
    # VARIÁVEIS
    string_cpf = ""
    lista_cpf = ""
    numero_valido = True
    contador1 = 10
    contador2 = 11
    variavel_acumuladora1 = 0
    variavel_acumuladora2 = 0
    primeiro_digito = 0
    segundo_digito = 0
    primeiro_digito_final = 0
    segundo_digito_final = 0
    string_numero_random = ""

    entrada = input(
        "Para gerar um CPF escolha [g]erar. Para sair digite [s]"
    )  # Pede para gerar um CPF

    if entrada.lower() == "g":  # Gera um cpf
        while numero_valido:  # Checa se o número não é composta de digitos iguais
            numero_random = random.randint(000000000, 999999999)
            string_numero_random = str(numero_random)

            if string_numero_random[0] * 9 == str(numero_random):
                continue
            else:
                break

        lista_cpf = list(
            str(numero_random)  # Cria uma lista com os 9 primeiros numeros
        )  # Mostra o cpf no padrão com pontos e traço

        lista_cpf.insert(3, ".")  # Insere os caracteres . e -
        lista_cpf.insert(7, ".")
        lista_cpf.insert(11, "-")

        for (  # Gera o priomeiro digito do cpf a partir dos outros 9 anteriores
            i
        ) in string_numero_random:
            if contador1 >= 2:
                calculo1 = contador1 * int(i)
                variavel_acumuladora1 += calculo1
                contador1 -= 1

        for (  # Gera o segundo digito do cpf a partir dos outros 10 anteriores
            j
        ) in string_numero_random:
            if contador2 >= 2:
                calculo2 = contador2 * int(j)
                variavel_acumuladora2 += calculo2
                contador2 -= 1

        primeiro_digito = (
            variavel_acumuladora1 * 10
        ) % 11  # Faz parte do calculo para o
        segundo_digito = (variavel_acumuladora2 * 10) % 11  # digito do cpf

        if primeiro_digito > 9:
            primeiro_digito_final = 0
        else:  # calcula o primeiro digito
            primeiro_digito_final = primeiro_digito

        if segundo_digito > 9:
            segundo_digito_final = 0
        else:  # calcula o primeiro digito
            segundo_digito_final = segundo_digito

        lista_cpf.append(
            str(primeiro_digito)
        )  # Adiciona a lista o primeiro digito calculado acima
        lista_cpf.append(str(segundo_digito))  # Adiciona o segundo digito a lista

        print("\nO CPF é :", "".join(lista_cpf), "\n")  # Printa o cpf já

    if entrada.lower() == "s":  # Sair do programa
        print("\nFim de programa\n")
        continuar_programa = False

    if (
        entrada.lower() != "g" and entrada.lower() != "s"
    ):  # Caso não digite uma das duas opções
        print("\nVocê não digitou uma opção válida\n")
        continue
