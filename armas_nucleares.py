matriz = []
indice = 1
def adcProduto(produto_input, preco_input):
    global linhas
    global indice
    linhas = [indice, produto_input, preco_input]
    indice += 1
    matriz.append(linhas)

def mostrarTodos():
    for linhas in matriz:
        print(' '.join(map(str, linhas)))

def removerProd(id):
    global indice
    for linhas in matriz:
        for espaco in linhas:
            if espaco == id:
                indice = matriz.index(linhas)
                matriz.remove(matriz[indice])
                break