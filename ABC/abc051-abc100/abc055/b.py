'''input
100000
457992974

3
6

10
3628800

'''


# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B


if __name__ == '__main__':
    from math import factorial

    training_count = int(input())
    print(factorial(training_count) % (10 ** 9 + 7))
