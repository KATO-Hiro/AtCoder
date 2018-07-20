# -*- coding: utf-8 -*-


def main():
    count = 0

    for i in range(12):
        if 'r' in input():
            count += 1

    print(count)


if __name__ == '__main__':
    main()
