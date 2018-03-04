'''input
2 2 2
2 1 2
2 2 2
'''

'''
1 0 1
2 1 2
1 0 1
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C


# HACK: More smartly.
def identify_a_and_b_from(grid_values):
    a = list()
    b = list()

    # Transform to equivalent expression.
    # (a1, a2, a3, b1, b2, b3)
    # = (p1 + x, p2 + x, p3 + x, q1 - x, q2 - x, q3 - x)
    # Because pi + qi = (pi + x) + (qi - x) holds.

    # It assumes that a1 = 0
    a.append(0)

    for j in range(3):
        b.append(grid_values[0][j] - a[0])

    for i in range(1, 3):
        a.append(grid_values[i][0] - b[0])
    return a, b


def satisfy_takahashi_information(grid_values, a, b):
    result = 'Yes'

    for i in range(0, 3):
        for j in range(0, 3):
            if grid_values[i][j] != a[i] + b[j]:
                return 'No'
    return result


if __name__ == '__main__':
    grid_values = [list(map(int, input().split())) for i in range(3)]

    # See:
    # https://img.atcoder.jp/abc088/editorial.pdf
    a, b = identify_a_and_b_from(grid_values)

    result = satisfy_takahashi_information(grid_values, a, b)
    print(result)
