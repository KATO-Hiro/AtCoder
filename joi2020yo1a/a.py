# -*- coding: utf-8 -*-


def main():
    numbers = list(map(int, input().split()))
    one = numbers.count(1)
    two = numbers.count(2)

    if one > two:
        print(1)
    elif one < two:
        print(2)


if __name__ == '__main__':
    main()
