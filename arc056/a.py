# -*- coding: utf-8 -*-


def main():
    from math import ceil
    a, b, k, l = list(map(int, input().split()))
    print(min(a * k, ceil(k / l) * b, k % l * a + k // l * b))


if __name__ == '__main__':
    main()
