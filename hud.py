from armas_nucleares import adcProduto, mostrarTodos, removerProd
global indice
total = 0
while True:
    print(f'''{"Lojinha do tadeu":-^50}''')
    user_input = int(input('''[1] Adicionar Produto e Preço
[2] Ver carrinho
[3] Finalizar compra
[4] Retirar produto
[5] Finalizar programa

Escolha: '''))
    if user_input == 1:
        while True:
            produto_input = input('Insira o Nome do produto: ')
            produto_sem_espaco = produto_input.replace(' ', '')
            if produto_sem_espaco.isalpha() == False:
                print('Insira apenas caracteres')
            else:
                break
        while True:
            try:
                preco_input = float(input('Insira o preço do produto: '))
            except ValueError:
                print('insira apenas numeros!')
            else:
                total += preco_input
                print('Produto adicionado no carrinho.')
            break
        adcProduto(produto_input, preco_input)

    if user_input == 2:
        mostrarTodos()

    if user_input == 3:
        print('Como você deseja efetuar o pagamento? ')
        print('1 - Cartão')
        print('2 - Dinheiro')
        pag = int(input(''))

        if pag == 1:
            print('O pagamento no cartão foi eftuado.')

        if pag == 2:
            dinheiro = float(input('Quanto você deseja pagar? '))
            troco = dinheiro - total
            print('O troco é: ',troco)

    if user_input == 4:
        while True:
            try:
                mostrarTodos()
                id = int(input('Escolha o ID de um produto para retirar: '))
            except ValueError:
                print('Coloque uma opção válida')
            else:
                removerProd(id)
                break
    if user_input == 5:
        print('Programa Finalizado.')
        break
