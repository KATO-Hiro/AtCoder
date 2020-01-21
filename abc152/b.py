# -*- coding: utf-8 -*-


def main():
    a, b = input().split()
    print(sorted([a * int(b), b * int(a)])[0])


if __name__ == '__main__':
    main()
