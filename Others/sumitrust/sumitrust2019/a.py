# -*- coding: utf-8 -*-


def main():
    m1, d1 = map(int, input().split())
    m2, d2 = map(int, input().split())

    if m1 == m2:
        print(0)
    else:
        print(1)


if __name__ == '__main__':
    main()
