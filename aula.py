# sempre tem colocar a funcao map em lista

# for i in range(0,3):
#     nomes[i] = nomes[i].upper()

# print(f'Aqui é nomes: {nomes}')
# deixar_maiusculo = lambda x: x.upper()
# nomes_maiusculos = list(map(lambda x: x.upper()))
# print(nomes_maiusculos)

def cumprimentar(nome:str):
    return f'Olá {nome}'

nomes = ['Prata','claudio','Joaquim']
cumprimentos = list(map(cumprimentar, nomes))
print(cumprimentos)

# filter tambem tem que usar a lista
nomes_com_p = list(filter(lambda x: x[0] == 0, nomes))
print(nomes_com_p)

numeros = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, numeros)
print(soma)