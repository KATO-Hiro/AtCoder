# -*- coding: utf-8 -*-


def main():
    n, x = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    a_max = max(a)
    count = 0

    for ai in a:
        if ai + x >= a_max:
            count += 1

    print(count)


if __name__ == '__main__':
    main()
