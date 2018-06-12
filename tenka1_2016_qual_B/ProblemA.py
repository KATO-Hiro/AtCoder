'''input

'''

# -*- coding: utf-8 -*-

# tenka1 2016 qual B
# Problem A


def f(n: int):
    from math import floor
    return floor((n ** 2 + 4.0) / 8.0)


if __name__ == '__main__':
    current_number = 20

    for i in range(3):
        result = f(current_number)
        current_number = result

    print(result)
