# -*- coding: utf-8 -*-


def main():
    a, b, c = map(int, input().split())

    if a + b >= c:
        print(b + c)
    else:
        print(a + b + 1 + b)


if __name__ == '__main__':
    main()
