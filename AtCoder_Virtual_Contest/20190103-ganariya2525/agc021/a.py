# -*- coding: utf-8 -*-


def main():
    n = list(map(int, input()))
    c = n[0]

    if len(n) > 1:
        k = set(n[1:])

        if len(k) == 1 and k == {9}:
            print(c + 9 * (len(n) - 1))
        else:
            print(c + 9 * (len(n) - 1) - 1)
    else:
        print(c)


if __name__ == '__main__':
    main()
