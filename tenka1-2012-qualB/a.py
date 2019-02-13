# -*- coding: utf-8 -*-


def main():
    a, b, c = map(int, input().split())

    for i in range(1, 128):
        if i % 3 == a and i % 5 == b and i % 7 == c:
            print(i)


if __name__ == '__main__':
    main()
