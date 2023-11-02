lista =[]
for i in range(6):
  lista.append(int(input('Ingrese número ganador: ')))
lista.sort()
print('Números ganadores: ')
print(*lista, sep=', ')