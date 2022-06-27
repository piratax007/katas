- [x] Leer el archivo
- [x] Clasificar el contenido del archivo por longitud de la palabra
- [x] Utilizar el tipo word y length para dar contexto
- [ ] Tomar tres palabras como entrada y verificar si los carácteres unidos de dos de ellas son los mismos que los de la tercera sin exceder el número de carácteres
- [ ] Recorrer el mapa de palabras seleccionando únicamente aquellas cuya suma de longitudes den una longitud específica (11 letras en "_documenting_")
- [ ] Verificar si todos los carácteres de las dos palabras seleccionadas del diccionarios están en la palabra dada (_"documenting"_)

---
```pseudo-code
dada una longitud l
si l es par:
    Se recorren las claves 1:l/2
        buscando las claves l/2:l-1

si l es impar:
    se recorren las claves 1:l//2
        buscando las claves l//2+1:l-1
```