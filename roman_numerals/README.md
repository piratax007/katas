# Roman Numerals Kata                                
(https://kata-log.rocks/roman-numerals-kata)

## Your Task

Write a method String convert(int) that takes a number and converts it to the according String representation.                                                                                                      
Examples
-    1 ➔ I
-    2 ➔ II
-    3 ➔ III
-    4 ➔ IV
-    5 ➔ V
-    9 ➔ IX
-   21 ➔ XXI
-   50 ➔ L
-  100 ➔ C
-  500 ➔ D
- 1000 ➔ M                                                                                                                                                                                                                     
** Hint                                                                                                                                                                                                                     
This kata lures a lot of people to implement features in the order of the numbers. But do not forget that it’s sometimes easier to start with a general case and add exceptions later.

## La lista

- [X] Debe recibir un número entero positivo menor que 9999
- [X] Debe separar un número dado en unidades, decenas, centenas, miles
- [X] Debe convertir el número de acuerdo a las siguientes reglas:
  - Si el número es menor que 4 utilizar el símbolo de la unidad tantas veces como el número i.e. número = 3 -> III
  - Si el número es 4, utilizar el símbolo de la unidad seguido del símbolo de 5
  - Si el número es 5, utilizar el símbolo equivalente
  - Si el número esta entre 6 y 9 utilizar el símbolo de 5 seguido del símbolo de la unidad tantas veces como la diferencia entre el número y 5
  - Si el número es 9, utilizar el símbolo de la unidad seguido del símbolo de la siguiente posición decimal