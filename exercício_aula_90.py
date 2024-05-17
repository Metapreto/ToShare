import os


lista_de_compras = []
deletar = 0
while True:
       
    
    menu_inicial = input(
        f'\nSelecione uma opção:\n[i]nserir  [a]pagar  [l]istar:'
        ).lower()
    
    
    
    if menu_inicial == 'i' or menu_inicial == 'a' or menu_inicial =='l':
        if menu_inicial == 'i':# Apaga o terminar, insere um nome na lista e retorna para o começo
            os.system('cls')
            produto = input(
                'Digite qual o produto: '
            )
            print('\n')
            lista_de_compras.append(produto)
            os.system('cls')

        if menu_inicial == 'a':#Apaga o terminar, deleta um item da lista e volta para o começo
            os.system('cls')
            if lista_de_compras == [] :#Condição caso a lista esteja vazia
                print('A lista está vazia')
                continue
            else:#Caso a lista não esteja vazia
                len(lista_de_compras)>0 
                deletar = input(
                'Qual item deseja apagar pelo indice?'
            )   
                if int(deletar) > (len(lista_de_compras) - 1):#Se o indice que deseja deletar está dentro da lista
                    print('Não foi possível deletar este item pois ele está vazio')

                else:#Caso o indice esteja dentro da lista
                    del lista_de_compras[int(deletar)]  

        if menu_inicial == 'l':#Mostra a lista e seus indices
            os.system('cls')
            for i, nome_produto in enumerate(lista_de_compras):
                print(i,nome_produto)    
    
    else:#Erro caso o valor no menu_inicial não seja valido
        
        print(
            '\nDesculpe, você não digitou um valor válido.\n'
            )
        
        continue


    
        
        