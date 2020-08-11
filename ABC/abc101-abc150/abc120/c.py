# -*- coding: utf-8 -*-


def main():
    s = input()
    zero_count = s.count('0')
    one_count = s.count('1')
    print(min(zero_count, one_count) * 2)


if __name__ == '__main__':
    main()
