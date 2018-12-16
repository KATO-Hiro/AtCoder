# -*- coding: utf-8 -*-


def main():
    c1, a = map(str, input().split())
    c2, b = map(str, input().split())

    if c1 == c2:
        print(abs(int(a) - int(b)) // 15)
    else:
        print(abs(int(a) + int(b)) // 15)


if __name__ == '__main__':
    main()
