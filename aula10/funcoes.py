#function em javascript
#func em goleng

#function que emptime texto na tela
def display():
    print('Olá mundo')
    
def cadastra_usuario():
    nome =input('Nome: ')
    idade =input('Idade: ')
    print(nome,idade)
    
def calcular_horas():
    valor_sal = float(input('Valor do salario: '))
    quantidade_horas = float(input('Quantidade de horas: '))
    cal = valor_sal/quantidade_horas
    print(f'O valor  hora é -> ,{cal:.2f}')
    extra = cal* 1.5
    print(f' Valor das horas extras -> ,{extra:.2f}')
    quantidade_horas_realizadas = float(input('Quantidade de horas extras: '))
    total = quantidade_horas_realizadas * extra
    print(f'Total de horas extras -> ,{total:.2f}')
    total_geral = valor_sal+ total
    print('O salarío é R$: ',valor_sal,'o total com horas extras',total_geral)
    
   
display()
cadastra_usuario()
calcular_horas()

# função que imprimi um texto na tela 



# def display():
#     print('olá')


# def cadastrar_usuario():
#     nome =  input('Nome:')
#     idade = int(input('Idade: '))
#     print(nome, idade)    


# def calculo_horas():
#     valor_sal = float(input('valor Salário'))
#     quatidade_horas  =  float(input('quantidade horas'))
#     cal =  valor_sal/quatidade_horas
#     print(f'valor hora -> {cal:.2f}')
#     extra  =  cal * 1.5
#     print('Hora extra -> ', extra)
#     diferenca =  extra - cal
#     print('Valor da extra -> ', diferenca)
#     quatidade_horas_realizadas =  float(input('Digite a quantidade de extra'))
#     total  =  quatidade_horas_realizadas * extra
#     print('Total de hora extra -> ', total)
#     total_geral = valor_sal +  total
#     print('Salário R$', total_geral)





# display()
# cadastrar_usuario()
# calculo_horas()