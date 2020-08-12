# -*- coding: utf-8 -*-


def main():
    l, x = map(int, input().split())
    ans = x % l

    if (x // l) % 2 != 0:
        ans = l - ans

    print(ans)


if __name__ == '__main__':
    main()
