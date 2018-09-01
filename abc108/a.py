# -*- coding: utf-8 -*-


def main():
    k = int(input())

    if k % 2 != 0:
        print(k // 2 * (k + 1) // 2)
    else:
        print((k // 2) ** 2)


if __name__ == '__main__':
    main()
