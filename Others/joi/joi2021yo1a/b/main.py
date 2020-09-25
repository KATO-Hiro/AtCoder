# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = input()
    j_count = s.count('J')
    o_count = s.count('O')
    i_count = s.count('I')

    print('J' * j_count + 'O' * o_count + 'I' * i_count)


if __name__ == '__main__':
    main()
