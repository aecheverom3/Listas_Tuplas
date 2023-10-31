lista = ['matemáticas', 'física', 'química', 'historia', 'lengua']
notas = []
for i in lista:
    nota = input('¿Qué nota has sacado en ' + i + '? ')
    notas.append(nota)
for j in range(len(lista)):
    print('En ' + lista[j] + ' has sacado ' + notas[j] + '.')
