import board as b
import ant as a

if __name__ == "__main__":
    tablero = b.Board(5, 5)
    hormiga = a.Ant(0, 0, "N")

    tablero.draw(hormiga)

    for _ in range(10):
        # print("--------------------------")
        # print(f"current ant position: ({hormiga.horizontal_position}, {hormiga.vertical_position})")
        # print(f"current ant direction: {hormiga.current_direction}")
        # print(f"current cell state: {tablero.states[hormiga.vertical_position][hormiga.horizontal_position]}")
        # print("--------------------------")
        hormiga.move(tablero)
        tablero.draw(hormiga)
        # print("--------------------------")
        # print(f"new ant direction: {hormiga.current_direction}")
        # print(f"new ant position: ({hormiga.horizontal_position}, {hormiga.vertical_position})")
        # print("--------------------------")
