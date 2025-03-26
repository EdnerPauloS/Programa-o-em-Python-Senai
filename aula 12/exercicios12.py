import os
import shutil

# # criar novo arquivo txt
# with open('exercicios', 'w') as arq:
#     os.mkdir('novo')

with open('exercicios', 'r', encoding='utf-8')as arquivo:
    conteudo = arquivo.read()
    print(conteudo)