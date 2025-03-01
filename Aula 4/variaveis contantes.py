NOME= 'JOSE'
NOME = 'MARIA'
#isso é um  contante nao altere
def imutavel():
    NOME = 'MARIA'
    return NOME
NOME = imutavel()
# e imutavel
print(NOME)
# trocas de typo de variaveis
numero = 10
print (type(numero))
mudou_1 = float(numero)
print (type(mudou_1))

texto = 'isso é um texto'
print (type(texto))
mudou_2 = bool(texto)
print (type(mudou_2))


logico = True
print (type(logico))
mudou_3 = int(logico)
print(type(mudou_3))

real = 5.2
print(type(real))
mudou_4 = str(real)
print(type(mudou_4))
