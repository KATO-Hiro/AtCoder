# -*- coding: utf-8 -*-


def main():
    height, bmi = list(map(float, input().split()))
    print((height / 100) ** 2 * bmi)


if __name__ == '__main__':
    main()
