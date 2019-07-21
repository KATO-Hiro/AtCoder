# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    sorted_a = sorted(a)
    a_max = max(a)
    a_second = sorted_a[-2]

    for ai in a:
        if ai == a_max:
            print(a_second)
        else:
            print(a_max)


if __name__ == '__main__':
    main()
