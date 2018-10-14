# -*- coding: utf-8 -*-


def main():
    n = int(input())
    r = list(map(int, input().translate(str.maketrans('ABCDF', '43210'))))
    print(sum(r) / n)


if __name__ == '__main__':
    main()
