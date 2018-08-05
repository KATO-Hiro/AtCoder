# -*- coding: utf-8 -*-


def main():
    s = input()
    numbers = [str(i) for i in range(0, 10)]
    result = ''

    for si in s:
        if si in numbers:
            result += si

    print(result)


if __name__ == '__main__':
    main()
