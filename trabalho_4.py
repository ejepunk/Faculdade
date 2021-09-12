
lista = []

def Cadastra_produto(produto_para_cadastrar: dict):
    lista.append(produto_para_cadastrar)
    return

opcao = int(input('cadastrar produto? 0 - Não  1 - Sim  '))
while opcao == 1:
    produto_novo = {}

    produto_novo['codico'] = int(input('Digite o codico do Produto: '))

    if produto_novo['codico'] == 0:
        print('Codico 0, encerrando cadastro de produtos.')
        break

    produto_novo['estoque'] = int(input('Digite a quantidade em estoque: '))
    produto_novo['minimo'] = int(input('Digite a quantidade minima em  estoque: '))

    Cadastra_produto(produto_novo)
    opcao = int(input('Cadastrar produto? 0 - Não  1 - Sim'))

if len (lista) > 0:
    print('lista de produtos por codico em ordem crescente:')
    print("codico".center(10), end='')
    print("estoque".center(10), end='')
    print("minimo".center(10))

    for produto in sorted(lista, key=lambda item:['codico']):
        print(str(produto['codico']).center(10),end='')
        print(str(produto['estoque']).center(10), end='')
        print(str(produto['minimo']).center(10))

    else:
        print('lista vazia.')
    print(f'Gustavo Pinheiro Antunes 25 ')

    ## Esse exercio eu faço um cadastro de produtos  e guarda em uma lista  e depois de todos adicionas são mostrados
    ## em uma lista e tambem pode ser intenropido quando achar necessario
    