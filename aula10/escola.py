# Desafio 1
# VOCÊ É UM DEV E PRECISA CRIAR UM SISTEMA PARA UMA ESCOLA. 
# SISTEMA DE NOTAS DE ALUNOS QUE MOSTRE COM ESTATISTICA A MODA
# E A MEDIA E DESVIO DE PADRÃO, DAS NOTAS DE ALUNOS DE UM COLÉGIO,
# ALÉM DE MOSTRAR MENOR E A  MAIOR NOTA, SEPARE EM FUNÇÕES DIFERENTES

alunos = {
    'Lucas': 0,
    'Mateus':0,
    'Felipe':0,
    'Daniel':0,
    'Paulo':0,
    'Eduardo':0
}


print('Nos temos os seguintes alunos: ',list(alunos.keys()))

for aluno in alunos:
    nota = float(input(f'Insira as notas dos {alunos} aqui: '))
    alunos[aluno]=nota
    

print('As notas dos alunos são: ')
for aluno, nota in alunos.items():
    print(f'{aluno}: {nota}')











## Desafio 2

# Você é um analista de dados, e decidiu trocar de emprego.

# Utilize a media, moda, mediana e o desvio padrão para decidir qual empresa faz sentido para você:

# Justificar por que decidiu por essa empresa.

# ***Verifique isso através dos salários:***

# empresa1 = [1000,6000,1200,8000,1400]

# empresa2 = [5000,4000,3000,2000,7000]

# empresa3 = [1200,1300,8000,3000,15000]

# empresa4 = [1400,1750,2000,4500,5900]