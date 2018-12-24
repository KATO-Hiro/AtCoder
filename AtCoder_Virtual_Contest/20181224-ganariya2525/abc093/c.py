# -*- coding: utf-8 -*-


def main():
    a, b, c = map(int, input().split())
    max_number = max(a, b, c)

    while True:
        diff = 3 * max_number - sum([a, b, c])

        if diff % 2 == 0:
            print(diff // 2)
            exit()
        else:
            max_number += 1


if __name__ == '__main__':
    main()
