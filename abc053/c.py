# -*- coding: utf-8 -*-


def main():
    x = int(input())
    result = x * 2 // 11

    if (x * 2 % 11 != 0) and ((x - 6) % 11 != 0):
        result += 1

    print(result)


if __name__ == '__main__':
    main()
