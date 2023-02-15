class Cat:
    def __init__(self, start: int, finish: int):
        self.start = start
        self.finish = finish
        self.distance = finish - start
        self.jump_Count = 0

    def jump_counter(self):
        if self.distance in [1, 3]:
            self.jump_Count += 1

        if self.distance == 2:
            self.start += 1
            self.jump_Count += 1
            self.distance -= 1
            self.jump_counter()

        if self.distance > 3:
            self.start += 3
            self.jump_Count += 1
            self.distance -= 3
            self.jump_counter()


def new_cat(start: int, finish: int) -> Cat:
    return Cat(start, finish)


def cats(start: int, finish: int) -> int:
    kitty = new_cat(start, finish)

    kitty.jump_counter()

    return kitty.jump_Count


if __name__ == '__main__':
    print(cats(98, 906))
