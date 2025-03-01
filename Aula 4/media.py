#variaveis
#sinais de comparaçao logico
#sinais de comparação aritmetico
#input/ output

nome = input('Digite o nome do Aluno: ')
nota1 =float(input('nota1: '))
nota2 =float(input('nota2: '))
nota3 =float(input('nota3: '))
nota4 =float(input('nota4: '))
nota5 =float(input('nota5: '))

media=(nota1 + nota2 +nota3 +nota4 +nota5)/5
print ('A media do Aluno:',nome,'foi iqual a: ',media)

requisito1 = media >= 7
requisito2 = media >= 5 and media <=6.9
requisito3 = media < 5

print (f'''
Situação do Aluno {nome}
APROVADO - {requisito1}
RECUPERAÇÃO -{requisito2}
REPROVADO -{requisito3}
''')
