import statistics


#control F para procurar no seu codigo 
#media
print()
lista = [11,12,11,12,11]
media = statistics.mean(lista)
print("Média:", media)
print()
# media_arredondada = round(media, 2)
# print("Média:", media_arredondada)
# print()
#mediana
mediana = statistics.median(lista)
print("Médiana:", mediana)
# m= sorted(lista)
# print("Médiana:", mediana)
#moda o que mais aparece
print()
entradas = [200,20,30,30,30,30,30,50,40]
moda = statistics.mode(lista)
print('Moda', moda)
#variança mosta a relacao entre a moda e o valor
print()
varianca = statistics.variance(lista)
print('Variança',varianca)