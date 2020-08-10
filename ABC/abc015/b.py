# -*- coding: utf-8 -*-


def main():
    from math import ceil

    n = int(input())
    a = list(map(int, input().split()))
    zero_count = sum([1 for ai in a if ai == 0])
    print(ceil(sum(a) / (n - zero_count)))


if __name__ == '__main__':
    main()
