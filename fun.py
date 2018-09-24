def main():
    add_two(3, 5)
    subtract_two(2, 1)
    multiply_two(5, 5)
    divide_by_three(add_three(1, 2, 3))


def add_two(v1, v2):
    """ do something
    """
    p = v1 + v2
    print(p)

    return p


def subtract_two(v1, v2):
    """ do more
    """
    p = v1 - v2
    print(p)

    return p


def multiply_two(v1, v2):
    """ multiply two numbers

    :param v1: number one
    :param v2: number two
    :returns: product number
    """
    p = v1 * v2
    print(p)

    return p


def add_three(v1, v2, v3):
    """ add three numbers

    :param v1: number one
    :param v2: number two
    :param v3: number three
    :returns: sum number
    """
    p = v1 + v2 + v3
    print(p)

    return p


def divide_by_three(num):
    """ divides a number by three

    :param num: the number to be divided
    :returns: quotient of num and three
    """

    return num/3


if __name__ == '__main__':
    main()
