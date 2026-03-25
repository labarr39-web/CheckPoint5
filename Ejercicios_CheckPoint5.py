# Uso de Función For

for contador in range(1,11):
    print(contador)
    

print('')
print('----------------------------')
print('')


# Función suma

def suma(a, b, c):
    return(a+b+c)


print(suma(3, 8, 14))

print('')
print('----------------------------')
print('')


# Función lambda

suma_3=lambda n1, n2, n3: n1+n2+n3
resultado=suma_3(3, 8, 14)
print(resultado)

print('')
print('----------------------------')
print('')


# Comprobar un valor en una lista

nombre = 'Enrique'

lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'


if nombre in lista_nombre:
    print(f'{nombre} se encuentra en la lista')
else:
    print(f'{nombre} no se encuentra en la lista')
    
