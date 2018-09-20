def main():
    add_two(3, 5)
    subtract_two(2, 1)
    multiply_two(5, 5)
    multiply_three(6, 6, 6)


def add_two(v1, v2):
    """ do something
    """
    p = v1 + v2
    print(p)


def subtract_two(v1, v2):
    """ do more
    """
    p = v1 - v2
    print(p)


def multiply_two(v1, v2):
    """ multiply two numbers

    :param v1: number one
    :param v2: number two
    :returns: product number
    """
    p = v1 * v2
    print(p)


def multiply_three(v1, v2, v3):
    """ multiply two numbers

    :param v1: number one
    :param v2: number two
    :param v3: number three
    :returns: product number
    """
    p = v1 * v2 * v3
    print(p)


if __name__ == '__main__':
    main()
