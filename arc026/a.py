# -*- coding: utf-8 -*-


def main():
    n, a, b = map(int, input().split())
    count_b = min(n, 5)

    print(min(n * a, (n - count_b) * a + b * count_b))


if __name__ == '__main__':
    main()
