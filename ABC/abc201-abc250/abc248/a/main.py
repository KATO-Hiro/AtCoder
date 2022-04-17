# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = list(input().rstrip())
    numbers = [i for i in range(10)]

    for number in numbers:
        if str(number) not in s:
            print(number)
            exit()


if __name__ == "__main__":
    main()
