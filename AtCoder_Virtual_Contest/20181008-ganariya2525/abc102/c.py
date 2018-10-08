# -*- coding: utf-8 -*-


def main():
    from statistics import median

    n = int(input())
    a = list(map(int, input().split()))
    mod_a = list()
    ans = 0

    for index, ai in enumerate(a, 1):
        mod_a.append(ai - index)

    b = int(median(mod_a))

    for mod_ai in mod_a:
        ans += abs(mod_ai - b)

    print(ans)


if __name__ == '__main__':
    main()
