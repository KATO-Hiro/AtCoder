# -*- coding: utf-8 -*-


def main():
    a, b = map(int, input().split())

    if a <= 9 and b <= 9:
        print(a * b)
    else:
        print(-1)


if __name__ == '__main__':
    main()
