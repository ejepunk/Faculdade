opcao = int(input('inserir dados? 0-não   1 - sim'))
while opcao == 1:
    aluno = input('Nome do aluno: ')
    nota = float(input('Nota final: '))

    if 0 <= nota < 3:
        conceito = 'E'
    elif 3 <= nota < 5:
        conceito = 'D'
    elif 5 <= nota < 7:
        conceito = 'C'
    elif 7 <= nota < 9:
        conceito = 'B'
    elif 9 <= nota <= 10:
        conceito = 'A'
    else:
        print('Nota Inválida, encerrando o programa.')
        exit()
    print(f"O aluno {aluno} tirou a nota {nota} e se enquadra no conceito {conceito}")
    opcao = int(input('Inserir dados? 0 - não   1 - sim' ))

    print(f'Gustavo Pinheiro Antunes 25 ')

## Nesse exercicio transfomei os numero em numeros real,   nome em uma variavel ,coloquei em laço de repetição
## para sempre addicionar uma nota  e mais pode ser interopido quando for necessario.