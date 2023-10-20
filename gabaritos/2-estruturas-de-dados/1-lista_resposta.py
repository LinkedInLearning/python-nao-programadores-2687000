# Crie uma lista apenas com elementos numéricos
anos = [1987, 2017, 2012, 1974]

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
pessoa = ['Crislaine', 36, 2010, ['python', 'r', 'javascript', 'ruby'], True, ['nadar', 'ler', 'pedalar'], False]

# Imprima na tela apenas os 5 primeiros elementos da lista
print(pessoa[:5])

# Crie um slice na lista para que imprima na tela os elementos de índice par
elementos_indice_par = pessoa[::2]
print(elementos_indice_par)

# Remova da lista o último item
pessoa.pop()
print(pessoa)

# Insira na lista um novo item
pessoa.append('calopsita')
print(pessoa)

# Remova da lista um item específico
pessoa.remove(2010)
print(pessoa)