## CheckPoint 5

   <br><br>

 1. ***¿Qué es un condicional?***  

    <br>

    Una condicional o declaración condicional permite controlar la toma de decisiones y las acciones que ejecutará el programa.  
    <br>
    Esto se consigue evaluando una condición, y dependiendo del resultado de esta, ya sea verdadera (`True`)  o falsa (`False`), el programa se bifurca ejecuatando unos comandos u otros.  

    <br>
    Para poder evaluar una condición se utilizan los operadores de comparación.

    A continuación se muestran cuales son

    <br><br>

    | Operador | Nombre | Descripción |
    |:--------:|:-------|:------------|
    | == |Igual | Comprueba si dos valores son iguales |
    | != | No es igual | Comprueba si dos valores son distintos |
    | > | Mayor que | Comprueba si el primer valor es mayor que el segundo |
    | < | Menor que | Comprueba si el primer valor es menor que el segundo |
    | >= | Mayor o Igual | Comprueba si el primer valor es mayor o igual que el segundo |
    | <= | Menor o Igual | Comprueba si el primer valor es menor o igual que el segundo |

    <br><br>

    Ejemplo:

    ```python
    print(3 > 4) # False
    print(3 < 4) # True
    print(3 == 4) # False
    print(4 == 4) # True
    print(3 != 4) # True
    print(3 >= 4) # False
    print(3 <= 4) # True
    ```

    <br><br>

    Es importante llevar una buena indexación del texto, ya que de ello depende que un comando sea ejecutado como parte de la condición o no.  
    <br>
    - Condicional ***IF... ELSE***

    Se trata de un sí condicional, es decir, si se cumple la condición se ejecutan una serie de comandos, y si no, se ejecutan otros.  
    <br>  
    Esta es su sintaxis

    <br>

    ```python
    if condición:
        # comandos a ejecutar si se cumple la condición.
    else:
        # comandos a ejecutar si NO se cumple la condición.
    ```

    <br><br>

    Las condicionales se pueden anidar para comprobar varias condicones, cada una dependiente del resultado de la anterior.

    Hay dos formas de implementarlo:  

    <br>

    Una  es introduciendo un segundo `if` dentro del primero, bien en la parte del `if` o dentro de la parte del `else`, todo depende de la casuistica que se necesite.  

    <br>  

    ```python
    if condición:
        # comandos a ejecutar si se cumple la condición.
    else:
        if condición2:
             # comandos a ejecutar si se cumple la condición.
        else:
            # comandos a ejecutar si NO se cumple la condición.
    ```  
    <br><br>  

    - ***IF... ELIF... ELSE***
    <br><br>

    La clausula elif (else if) permite implementar una segunda condición en la parte del `else` con una sola instrucción, pudiendo anidarse tantas como sean necesarias.

    <br>

    ```python
    if condición1:
        # comandos a ejecutar si se cumple la condición.
    elif condición2:
            # comandos a ejecutar si NO se cumple condición1 pero SI condición2.
    else:
        # comandos a ejecutar si NO se cumple ninguna de las condiciones.
    ```

    <br><br>

 2. ***¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?***  

    <br>

    Comencemos por saber qué es un bucle en programación.  
    <br>
    Un bucle es un conjunto de acciones que se repiten un número determinado de veces, hasta que se cumpla una condición, o hasta que se le indique mediante un comando que debe salir de él.  
    <br>
    Resultan esenciales cuando se trata de acciones repetitivas, como por ejemplo buscar algo en una lista o diccionario.  
    <br>

    En Python hay dos estructuras para ello:  
    <br>
    - ***FOR.. IN... :***  
    <br>

    Se usa para iterar sobre una secuencia (como una lista, tupla, cadena o rango) y ejecutar un bloque de código para cada elemento en esa secuencia.  
    <br>  

    Hay que tener en cuenta que la palabra que sigue a `for` es el nombre de una variable que se crea con el único fin de ser un 'contador' dentro del bucle, y la palabra que sigue a `in` es el objeto que se va a recorrer (en estos ejemplos una lista y una cadena).  
    <br>

    A continuación se muestra un ejemplo de cómo usar un bucle `for` para recorrer una lista e imprimir cada idioma en la consola:  

    <br>  

    ```python
    lenguajes_programacion = ['Rust', 'Java', 'Python', 'C++']

    for lenguaje in lenguajes_programacion:
        print(lenguaje)

    """
    Resultado 

    Rust
    Java
    Python
    C++
    """
    ```  


    <br>  

    En este ejemplo se usa un bucle for para recorrer la cadena código y escribir cada carácter:  
    <br>

    ```python  
    for caracter in 'codigo':
    print(caracter)

    """
    Resultado 

    c
    ó
    d
    i
    g
    o
    """
    ```  
    <br><br>  
    Al igual que los condicionales, los bucles también pueden anidarse.  
    <br>
    Aquí puede verse un ejemplo de bucles `for` anidados.  
    <br>

    ```python
    columnas=['A', 'B']
    filas=[1, 2, 3]

    for columna in columnas:
        for fila in filas:
            print(columna, fila)

    '''
    Resultado

    A 1
    A 2
    A 3
    B 1
    B 2
    B 3
    '''
    ```  
    <br><br>
    - ***WHILE... :***  
    <br>

    Con `while` se repite un bloque de código mientras se cumpla la condición.  
    <br>
    Este ejemplo muestra el uso de `while`. En este caso se repetirá el bucle mientras no se acierte el número secreto.  
    <br>  


    ```python
    numero_secreto = 3
    numero_usuario = 0

    while numero_usuario != numero_secreto:
        numero_usuario = int(input('Introduce un número del 1 al 5: '))
        if numero_usuario != numero_secreto:
            print('¡Error!, vuelve a intentarlo')

    print('¡Lo lograste!')

    """
    Resultado

    Introduce un número del 1 al 5: 2
    ¡Error!, vuelve a intentarlo
    Introduce un número del 1 al 5: 1
    ¡Error!, vuelve a intentarlo
    Introduce un número del 1 al 5: 3
    ¡Lo lograste!
    """
    ```  
    <br><br>  
    - ***BREAK y CONTINUE***  
    <br>

    `break` y `continue` se usan en bucles para modificar la ejecución del mismo.  
    <br>
    La declaración `break` se usa para salir del bucle inmediatamente cuando una cierta condición se cumple.  
    <br>
    Aquí hay un ejemplo de cómo usar la declaración break con una lista de nombres:  
    <br>
    ```python
    nombres = ['Jose', 'Pedro', 'Pablo']

    for nombre in nombres:
        if nombre == 'Pedro':
            break
        print(nombre)
    
    '''
    Resultado

    Jose
    '''
    ```  
    <br>  

    En este caso comprueba si el nombre es igual a 'Pedro', si lo es, sale del bucle, si no lo es imprime el nombre.  
    <br><br>
    La declaración `continue` se usa para saltar la iteración actual y pasar a la siguiente iteración del bucle.  
    <br>
        Aquí hay un ejemplo de cómo usar la declaración continue:  
     <br>  
     ```python
    nombres = ['Jose', 'Pedro', 'Pablo']

    for nombre in nombres:
        if nombre == 'Pedro':
            continue
        print(nombre)
    
    '''
    Resultado

    Jose
    Pablo
    '''
    ```  
    <br>  
    En este ejemplo, al contrario que en el anterior, si nombre no es igual a 'Pedro', imprime nombre, pero si se cumple la condición, ignora el resto de instrucciones que hay en el bucle y vuelve a ejecutar el ciclo con el siguiente elemento.  
    <br>
    Por eso imprime todos los nombres menos 'Pedro'.  
<br><br>  
  
 3. ***¿Qué es una lista por comprensión en Python?***  
 
    <br>  
    La lista por comprensión permite agrupar un bucle e incluso un condicional, y asignar el resultado a una variable; todo ello en una sola línea de código en lugar de hacerlo en varias.  
    <br><br>  

    ```python
    numeros_pares = [num for num in range(1, 21) if num % 2 == 0]
    
    print(numeros_pares)

    '''
    Resultado

    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    '''
    ```  
    <br>  
    Este código añade a numeros_pares el valor de num en cada iteración si num es divisible por 2.  

    <br><br>  

    El ejemplo anterior es equivalente al siguiente código  
    <br>  

    ```python
    numeros_pares = []

    for num in range(1,21):
        if num % 2 == 0:
            numeros_pares.append(num)
    
    print(numeros_pares)

    '''
    Resultado

    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    '''
    ```  
    <br><br>  

 1. ***¿Qué es un argumento en Python?***  

    <br>    
    En Python, un argumento es el valor concreto que le pasas a una función cuando la llamas. Es distinto del parámetro, que es la variable definida en la firma de la función y que recibe ese valor.  
    
    <br>  
    

    - *Parámetro vs argumento*  

        Parámetro:  
    La variable en la definición de la función  
        <br>

        ```python
        def sumar(a, b):
        # a y b son parámetros
        ```  
       <br>  

        Argumento:  

        El valor que se pasa al llamar  

       <br>  

        ```python
        sumar(2, 3)
        # 2 y 3 son argumentos
        ```
    <br>  


    - *Argumentos posicionales y por palabra (keyword)*  

        Posicionales:  
        
        El orden importa.  
        <br>

        ```python
        def f(x, y): ... f(1, 2)
        '''
        1 → x, 2 → y

        No es lo mismo x/y que y/x
        '''
        ```  
        <br>  

        Por palabra:  
        
        Indicas el nombre del parámetro; al indicarse con un nombre, el orden no importa.  
        <br>

        ```python
         f(y=2, x=1)
         # El orden no importa
        ```  
        <br>

        Valores por defecto:  

        Puedes dar un valor por defecto a parámetros; si no pasas argumento, se usa ese valor  
        <br>

        ```python
        def saludar(nombre="mundo"):
            print("Hola", nombre)
            
        saludar()
        # Hola mundo
        
        saludar("Ana")
        # Hola Ana
        ```  
        <br><br>  


 1. ***¿Qué es una función Lambda en Python?***  

    <br>  
    Una función lambda en Python es una forma concisa de crear una función sin un nombre (una función anónima).  
        
    <br>  
    Las funciones lambda a menudo se usan como argumento para otra función.  
    
    <br>  
    Aquí hay un ejemplo de una función lambda  

    <br>

    ```python
    numbers = [1, 2, 3, 4, 5]

    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(even_numbers)
    
    '''
    Resultado
    
    [2, 4]
    '''
    ```
    <br>
    En este ejemplo, tenemos una lista de números y queremos crear una nueva lista de números pares. Entonces, pasamos una función lambda como uno de los argumentos a la función filter() para obtener una nueva lista que contiene los números 2 y 4.  

    <br>  

    Al trabajar con funciones lambda, es importante estar al tanto de las mejores prácticas; estas incluyen no asignarlas a una variable, mantenerlas simples y legibles, y usarlas para funciones cortas y puntuales.  

    Veamos algunos ejemplos  
    
    <br>  

    ```python
    numeros = [1, 2, 3, 4, 5]

    cuadrado = lambda x: x * x
    numeros_cuadrado = list(map(cuadrado, numeros))
    print(numeros_cuadrado)
    
    '''
    Resultado
    
     [1, 4, 9, 16, 25]
     '''
    ```  
    <br>  

    Esto va en contra del propósito de usar funciones anónimas. En este caso, se debería usar una función regular, así:  
    <br>  
    
    ```python
    numeros = [1, 2, 3, 4, 5]

    def cuadrado(num):
        return num * num

    numeros_cuadrado = list(map(cuadrado, numeros))
    print(numeros_cuadrado)
    
    '''
    Resultado
    
    [1, 4, 9, 16, 25]
    '''
    ```  
    <br>  

    Además, se debe evitar crear funciones lambda que sean difíciles de leer o innecesariamente complicadas, como esta:  
    <br>  

    ```python
    result = (lambda x: (x**2 + 2*x - 1) if x > 0 else (x**3 - x + 4))(3)

    print(result)
    
    '''
    Resultado
    
    14
    '''
    ```  
    <br>  

    Aunque esta función se ejecuta bien y produce el resultado correcto (14), no es fácil de leer ni de entender.  
    <br>
    En este caso, sería mejor crear una función separada con una estructura if/else, y luego llamar a esa función  
    <br>  

    ```python
    def calcular_expresion(x):  
        if x > 0:
            return x**2 + 2*x - 1
        else:
            return x**3 - x + 4

    print(calcular_expresion(3))
    
    '''
    Resultado
    
    14
    '''
    ```  
    <br>  

    Tanto las funciones regulares como las funciones lambda tienen sus casos de uso en programas de Python.  
    <br>
    Si se está trabajando con una sola expresión en línea, entonces se podría considerar usar una función lambda. De lo contrario, usar una función regular sería la mejor opción.



    <br><br>  


 1. ***¿Qué es un paquete pip?***  

    <br>
    Un paquete pip es un conjunto de módulos o librerías de Python que están empaquetados y publicados en PyPI para que puedan ser instalados fácilmente usando pip. Estos paquetes pueden contener código reutilizable, herramientas, frameworks, o cualquier tipo de funcionalidad que se pueda importar y usar en proyectos Python.  

    <br>  
    ¿Qué es pip?  
    
    <br>

    Pip es una herramienta que permite instalar, actualizar y desinstalar paquetes de Python desde el repositorio oficial llamado [PyPI](https://pypi.org) (Python Package Index). Facilita la gestión de bibliotecas y módulos que los desarrolladores pueden usar para ampliar las funcionalidades de sus programas.  

    <br>

    Ejemplo de uso:  

    <br>
    Para instalar un paquete, por ejemplo requests (una librería para hacer solicitudes HTTP), se usa el comando en la terminal  

    <br>  
    

    ```
    pip install requests
    ```  
    <br>
    Esto descarga e instala el paquete requests y sus dependencias para que pueda usarse en el código.