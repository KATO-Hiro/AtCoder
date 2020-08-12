# -*- coding: utf-8 -*-


def main():
    a, b = map(int, input().split())

    if a + 0.5 - b > 0:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()
