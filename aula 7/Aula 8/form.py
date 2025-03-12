#control D a palavra selecionada vai ser toda alteradas ao mesmo tempo
# control : serve pra comentar todos os codigos selecionados

form_user = {
'nome':None,
'idade':None,
'endereço':None,
'cursos':0,
}

nome1 = input('nome: ')
idade1 = input('idade: ')
endereco1 = input('endereco: ')
cursos1 = input('cursos: ')
cursos2 = input('cursos: ')
cursos3 = input('cursos: ')
lista_cursos = []
lista_cursos += (cursos1,cursos2,cursos3)

form_user['nome'] =  nome1
form_user['idade'] =  idade1
form_user['endereço'] =  endereco1
form_user['cursos'] =  lista_cursos


print(form_user['cursos'])

