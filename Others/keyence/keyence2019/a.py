# -*- coding: utf-8 -*-


def main():
    n = list(map(int, input().split()))
    numbers = [1, 9, 7, 4]

    for number in numbers:
        if n.count(number) != 1:
            print('NO')
            exit()

    print('YES')


if __name__ == '__main__':
    main()
