# -*- coding: utf-8 -*-


def main():
    a, b = map(int, input().split())
    patten1 = [1, 2, 3, 2, 1]
    patten2 = [2, 3, 3, 2, 1]

    if a == b:
        print(0)
        exit()

    diff = abs(b - a)
    p, q = divmod(diff, 10)

    if 1 <= q <= 5:
        if p >= 1:
            print(p + patten1[q - 1])
        else:
            print(patten1[q - 1])
    else:
        if q == 0:
            print(p)
            exit()

        if p >= 1:
            print(p + patten2[q - 6])
        else:
            print(patten2[q - 6])


if __name__ == '__main__':
    main()
