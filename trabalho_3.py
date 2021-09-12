import random

doadores = []

def cadastrar_doadores(nome:str, doacao:float):
    doadores.extend( ((nome + ' ') * int(doacao//10)).split() )
    return
def sorteio_ganhador():
    random.shuffle(doadores)
    print((f'Lista de doadores embaralhada'))
    return random.choice(doadores)

opcao = int(input('Cadastrar doador ? 0 - Não   1 - Sim '))

while  opcao == 1:
    doador = input('Nome do doador: ')
    valor = float(input('Valor da doaÇão: '))

    while len (doador.strip()) == 0 or valor < 10:
        print('O nome é obrigatorio e o valor minimo para a doação e de R$ 10')
        doador = input ('Nome do doador: ')

    cadastrar_doadores(doador, valor)

    opcao = int(input('cadastrar doador? 0 - Não  1 - Sim'))

if len(doadores) > 0:
    print(f'Lista de doadores para sorteio: {doadores}')
    print(f'o vencedor(a) foi: {sorteio_ganhador()}')
    print(f'Gustavo Pinheiro Antunes 25 ')


    ## Nesse exercicio trabalho com uma lista que gorda nomes e dinheiro enquando for adicionados nomes e valores de
    ## de doacão o progra fica no loop e logo quando sair ele faz um sorteio de ganhadores que foi adicionado na lista