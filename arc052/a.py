# -*- coding: utf-8 -*-


def main():
    s = input()
    result = ''

    for si in s:
        if si.isdigit():
            result += si

    print(result)


if __name__ == '__main__':
    main()
