# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    s = input()

    one = s.count('1')
    two = s.count('2')
    three = s.count('3')
    four = s.count('4')

    print(max(one, two, three, four), min(one, two, three, four))


if __name__ == '__main__':
    main()
