# Nesse projeto vamos criar um script que passará por todos os cursos de uma trilha profissional e imprimirá na tela a informação sobre o n;ivel atual de cada curso
# 1. Crie um dicionário para reunir as seguintes informações sobre a trilha profissional: a sequencia dos cursos, título do curso e total de níveis
# 2. Atribua a uma variável uma lista apenas com a sequencia dos cursos
# 3. Crie um for loop para passar por todos os cursos
# 4. Em cada loop, imprima mensagens informando sobre o nível atual do curso, do primeiro ao último nível (dica: realize o loop de níveis usando while loop)
# 5. Ao final imprima na tela a informação de que a trilha profissional foi concluída com sucesso

trilha = {1: {'curso': 'Introdução a SQL', 'total_niveis': 3}, 2: {'curso': 'Python: Formação Básica', 'total_niveis': 7}}

trilha_niveis = list(trilha.keys())
curso_nivel_atual = 1

for nivel in trilha_niveis:
    curso_atual = trilha[nivel]['curso']
    curso_total_niveis = trilha[nivel]['total_niveis']

    print(f'\n\nBem vinda ao curso "{curso_atual}"!. Você está iniciando o curso no nível {curso_nivel_atual}.\n........')
    
    while curso_nivel_atual <= curso_total_niveis:
        print(f'Parabéns! Você acaba de concluir a fase {curso_nivel_atual} do curso "{curso_atual}".')
        curso_nivel_atual += 1
    else:
        curso_nivel_atual = 1

else:
    print('\n\nVocê concluiu a trilha profissional com sucesso!!')