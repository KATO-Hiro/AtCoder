# -*- coding: utf-8 -*-


def main():
    s = input().split('+')
    count = 0

    for si in s:
        if '0' not in si:
            count += 1

    print(count)


if __name__ == '__main__':
    main()
