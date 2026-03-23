#####################################
#                                   #
#        Función  FizzBuzz          #
#                                   #
#####################################

'''
        función FizzBuzz            
                                   
 Argumento: Valor Final de la Lista
 
 Imprime desde 1 hasta Fin de Lista                                    
 Si es múltiplo de 3 imprime 'Fizz'
 Si es múltiplo de 5 imprime 'Buzz'
 Si es múltiplo de ambos imprime 'FizzBuzz'
 
'''


def FizzBuzz(valor_maximo):
    for num in range(1, valor_maximo + 1):
        if (num % 3 == 0 and num % 5 == 0):
            print('FizzBuzz')
        elif (num % 3 == 0):
            print('Fizz')
        elif (num % 5 == 0):
            print('Buzz')
        else:
            print(num)
    return

FizzBuzz(100)

