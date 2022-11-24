from armas_nucleares import adcProduto, mostrarTodos
while True:
    print(f'''{"Lojinha do tadeu":-^50}''')
    user_input = int(input('''[1] Adicionar Produto e Preço
[2] Ver carrinho
[3] Finalizar compra
[4] Retirar produto

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
                print('Agradecemos pela sua compra!')
            break
        adcProduto(produto_input, preco_input)

    if user_input == 2:
        mostrarTodos()


#if user_input == 3:
    #print('Compra finalizada foda')
    #   Parte do cauã
    #   Tambem parte do total

