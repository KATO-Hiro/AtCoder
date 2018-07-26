# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


def main():
    n, a, b = list(map(int, input().split()))
    position = 0

    for i in range(n):
        s, d = list(map(str, input().split()))

        if int(d) < a:
            d = a
        elif int(d) > b:
            d = b
        else:
            d = d

        if s == 'West':
            d = -1 * int(d)
        else:
            d = int(d)

        position += d

    if position == 0:
        print(str(0))
    elif position > 0:
        print('East ' + str(position))
    else:
        print('West ' + str(abs(position)))


if __name__ == '__main__':
    main()
