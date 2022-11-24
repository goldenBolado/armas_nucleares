matriz = []
def adcProduto(produto_input, preco_input):
    global linhas
    linhas = [produto_input, preco_input]
    matriz.append(linhas)

def mostrarTodos():
    for linhas in matriz:
        print(' '.join(map(str, linhas)))
