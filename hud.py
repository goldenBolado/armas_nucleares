from armas_nucleares import adcProduto, mostrarTodos, removerProd
global indice
while True:
    print(f'''{"Lojinha do tadeu":-^50}''')
    user_input = int(input('''[1] Adicionar Produto e Preço
[2] Ver carrinho
[3] Finalizar compra
[4] Retirar produto

Escolha: '''))
    if user_input == 1:
        total = 0
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
                print('Agradecemos pela sua compra!')
            break
        adcProduto(produto_input, preco_input)

    if user_input == 2:
        mostrarTodos()

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


#if user_input == 3:
    #print('Compra finalizada foda')
    #   Parte do cauã
    #   Tambem parte do total

