# -*- coding: utf-8 -*-


def main():
    n = int(input())
    x = list(map(int, input().split()))
    m = int(input())
    a = list(map(int, input().split()))

    for ai in a:
        pos = x[ai - 1]

        if (pos + 1) >= 2020:
            pass
        elif (pos + 1) not in x:
            x[ai - 1] += 1

    for xi in x:
        print(xi)


if __name__ == '__main__':
    main()
