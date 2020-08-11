# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = input()
    count = s.count('a')
    count += s.count('i')
    count += s.count('u')
    count += s.count('e')
    count += s.count('o')

    print(count)


if __name__ == '__main__':
    main()
