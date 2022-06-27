# Langton Ant List

# BL
- [X] Un objeto ant
  - **Atributos**
    - Tiene una posición
    - Tiene una dirección

- [X] Un objeto tablero
  - **Atributos**
    - Tiene dos dimensiones: Número de filas y número de celdas por fila (columnas)
    - Tiene una grilla compuesta de celdas
  - **Métodos**
    - [X] Reglas
      - **Inputs**
        - La dirección actual de la hormiga
        - La posición actual de la hormiga
      - **Outputs**
        - La dirección que debe tomar la hormiga 
        - La nueva posición de la hormiga
          1. En una celda blanca:
             1. Nueva dirección: 90 grados a la derecha 
             2. Nuevo color: Negro
             3. Desplazamiento: Una celda en la Nueva Dirección
          2. En una celda negra:
             1. Nueva dirección: 90 grados a la izquierda 
             2. Nuevo color: Rojo
             3. Desplazamiento: Una celda en la Nueva Dirección
          3. En una celda roja:
             1. Nueva dirección: No rota 
             2. Nuevo color: Blanco
             3. Desplazamiento: Una celda en la Nueva Dirección
          4. Si la hormiga está en la última columna y la nueva dirección es al Este (E), la desplaza a la primera columna de la fila
          5. Si la hormiga está en la primera columna y la nueva dirección es al Oeste (W), la desplaza a la última columna de la fila
          6. Si la hormiga está en la primera fila y la nueva dirección es al Norte (N), la desplaza a la última fila
          7. Si la hormiga está en la última fila y la nueva dirección es al Sur (S), la desplaza a la primera fila 
  
  - [X] un objeto celda
    - **Atributos**
      - Tiene una posición
      - Tiene un color
    - **Métodos**
      - [X] Cambiar color
        - **Inputs**
          - El nuevo color

# GUI

# main