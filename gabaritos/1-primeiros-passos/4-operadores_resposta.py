ano_nascimento = 1989
ano_formatura = 2010

# Considerando que as variáveis acima correspondem a 'Gerlaine', descubra a idade dela no ano da sua formatura
idade = ano_formatura - ano_nascimento

# Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas
print(ano_nascimento > ano_formatura)
print(ano_nascimento <= ano_formatura)
print(ano_nascimento == ano_formatura)

# Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas
print((ano_nascimento > ano_formatura) and (ano_nascimento > ano_formatura))
print((ano_nascimento <= ano_formatura) or (ano_nascimento > ano_formatura))
print(not(ano_nascimento == ano_formatura))