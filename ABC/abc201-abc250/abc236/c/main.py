# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    s = list(input().split())
    t = set(input().split())

    for si in s:
        if si in t:
            print('Yes')
        else:
            print('No')


if __name__ == "__main__":
    main()
