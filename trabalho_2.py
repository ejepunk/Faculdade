def escreve_email(nome: str, sobrenome: str):
    if len(nome) > 0 and len(sobrenome) > 0:
        return nome[0] + sobrenome + '@algoritimo.com.br'


print(escreve_email('gus', 'pinheiro'))
print(f'Gustavo Pinheiro Antunes 25 ')

## Nesse exercicio estou trabalando para escrever o nome e sobre nome e tranformar em email