# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    sorted_a = sorted(a)
    a_max = max(a)

    for ai in a:
        if ai == a_max:
            print(sorted_a[-2])
        else:
            print(sorted_a[-1])


if __name__ == '__main__':
    main()
