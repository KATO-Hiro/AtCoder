# -*- coding: utf-8 -*-


def main():
    h, bmi = map(float, input().split())

    print(h ** 2 / 10000 * bmi)


if __name__ == '__main__':
    main()
