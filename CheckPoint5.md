## CheckPoint 5

   <br><br>

 1. ***¿Qué es un condicional?***

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

    <br><br>  

    - ***IF... ELIF... ELSE***
<br><br>

    ```python
    if condición:
        # comandos a ejecutar si se cumple la condición.
    else:
        if condición2:
             # comandos a ejecutar si se cumple la condición.
        else:
            # comandos a ejecutar si NO se cumple la condición.
    ```

<br>

La clausula elif (else if) permite implementar una segunda condición con una sola instrucción

<br><br>

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

1. ***¿Qué es una lista por comprensión en Python?***

2. ***¿Qué es un argumento en Python?***

3. ***¿Qué es una función Lambda en Python?***

4. ***¿Qué es un paquete pip?***
