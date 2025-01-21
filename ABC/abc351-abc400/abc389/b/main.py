# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x = int(input())
    number = 1

    for i in range(1, 100):
        number *= i

        if number == x:
            print(i)
            exit()


if __name__ == "__main__":
    main()
