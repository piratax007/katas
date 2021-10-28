from math import sqrt
import operator as op


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
    operators = {"+": op.add, "-": op.sub, "/": op.truediv, "*": op.mul, "SQRT": sqrt, "MAX": max}
    stack = []
    for item in numbers_operators_list:
        if type(item) is not str:
            stack.append(item)
        else:
            # TODO: implement the sqrt ans max operators
            second_operand = stack.pop()
            first_operand = stack.pop()
            new_item = operators[item](first_operand, second_operand)
            stack.append(new_item)

    if len(stack) > 1:
        solver(stack)
    else:
        return stack.pop()


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print(cast("3.14"))
#     print(type(cast("3.14")))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
