# -*- coding: utf-8 -*-


def main():
    n = int(input())
    count = 0

    for i in range(1, 100 + 1):
        if i % n != 0:
            count += 1

    print(count)


if __name__ == '__main__':
    main()
