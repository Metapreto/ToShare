"""
746.824.890-70
"""

mensagem_erro = "O CPF digitado não é um cpf Válido"
abertura = "Digite um CPF com os pontos e traço.\nEx: 000.000.000-00: "
cpf_numero = 0
calculo_primeiro_digito = 0
calculo_segundo_digito = 0
primeiro_digito = 0
segundo_digito = 0
numero_condicional1 = 0
numero_condicional2 = 0


while True:  # inicia o validador
    contador_regresso_p1 = 10
    contador_regresso_p2 = 11
    calculo_primeiro_digito = 0
    calculo_segundo_digito = 0
    cpf = input(abertura)

    if cpf[3] != "." or cpf[7] != "." or cpf[11] != "-":  # testa o formato do CPF
        print("\n", mensagem_erro, "\n")
    else:  # formata o cpf para que não tenha pontos e traços
        lista_digitos = list(cpf)
        lista_digitos.remove(".")
        lista_digitos.remove(".")
        lista_digitos.remove("-")

        for (
            i
        ) in lista_digitos:  # Faz os calculos para encontrar o primeiro digito do cpf
            if contador_regresso_p1 >= 2:
                calculo1 = int(i) * contador_regresso_p1
                calculo_primeiro_digito += calculo1
                contador_regresso_p1 -= 1
            else:
                break
        numero_condicional1 = (calculo_primeiro_digito * 10) % 11
        if numero_condicional1 > 9:
            primeiro_digito = 0
        else:
            primeiro_digito = numero_condicional1

        for (
            j
        ) in lista_digitos:  # Faz os calculos para encontrar o segundo digito do cpf
            if contador_regresso_p2 >= 2:
                calculo2 = int(j) * contador_regresso_p2
                calculo_segundo_digito += calculo2
                contador_regresso_p2 -= 1
            else:
                break
        numero_condicional2 = (calculo_segundo_digito * 10) % 11
        if numero_condicional2 > 9:
            segundo_digito = 0
        else:
            segundo_digito = numero_condicional2

        # teste se os resultados são iguais ao do cpf digitado
        if primeiro_digito == int(cpf[12]) and segundo_digito == int(cpf[13]):
            print("\nO cpf é válido\n")
        else:
            print("o cpf é invalido\n")
        # print(numero_condicional)
