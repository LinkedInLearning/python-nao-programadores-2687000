# Declare 4 variáveis do tipo numérica
x = 4
y = 30
a = 3
e = 66

# Crie uma estrutura condicional para comparar dois números
if x > y:
    print(True)
else:
    print(False)

# Se a condição for verdadeira, imprima na tela uma mensagem informando que a condição foi cumprida e informando o número de maior valor
if x > y:
    print(f'A condição foi cumprida. O número {x} é maior do que {y}')
else:
    print(False)

# Se a condição não for cumprida, imprima na tela uma mensagem informando que a condição é negativa e informe o número de maior valor
if x > y:
    print(f'A condição foi cumprida. O número {x} é maior do que {y}')
else:
    print(f'A condição não foi cumprida. Na verdade, o número {y} é maior do que {x}')

# Insira outras condições na estrutura condicional usando o elif
if x > y:
    print(f'A condição foi cumprida. O número {x} é maior do que {y}')
elif x > a:
    print(f'Nesse caso, verificamos que o número {x} é maior do que {a}')
else:
    print(f'A condição não foi cumprida. Na verdade, o número {y} é maior do que {x}')

# Incremente a estrutura condicional já existente com expressões lógicas utilizando "and" ou "or"
if (x > y) or (x > a):
    print(f'A condição foi cumprida. O número {x} é maior do que {y}')
elif (x == a) and (e > y):
    print(f'Nesse caso, verificamos que o número {x} é maior do que {a}')
else:
    print(f'A condição não foi cumprida. Na verdade, o número {y} é maior do que {x}')

# Crie uma estrutura condicional onde mais de uma condição seja verdadeira, e use apenas a palavra reservada "if"
if y > a:
    print(f'A condição foi cumprida. O número {y} é maior do que {a}')
if e > x:
    print(f'Nesse caso, verificamos que o número {e} é maior do que {x}')