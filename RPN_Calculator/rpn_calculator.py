from math import sqrt


def cast(char: str):
    """
    if char is a number (int or float) cast to the correspondent type else return the same string
    :return: int or float or string
    """
    for t in (int, float, str):
        try:
            n = t(char)
            return n
        except ValueError:
            pass


def user_input(str_in: str) -> list:
    characters = str_in.split(" ")
    return characters


def cast_characters(char_list: list) -> list:
    int_str_list = [cast(char) for char in char_list]
    return int_str_list


def solver(numbers_operators_list: list):
    stack = []
    for item in numbers_operators_list:
        if type(item) is not str:
            stack.append(item)
        elif item == "SQRT":
            stack.append(sqrt(stack.pop()))
        else:
            second_operand = str(stack.pop())
            first_operand = str(stack.pop())
            new_item = eval(first_operand + item + second_operand)
            stack.append(new_item)

    return stack.pop()


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print(cast("3.14"))
#     print(type(cast("3.14")))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
