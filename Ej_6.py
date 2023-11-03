asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
aprobadas = []
for i in asignaturas:
    score = float(input('¿Qué nota has sacado en ' + i + '?'))
    if score >= 5:
        aprobadas.append(i)
for j in aprobadas:
    asignaturas.remove(j)
print('Tienes que repetir ' + str(asignaturas))