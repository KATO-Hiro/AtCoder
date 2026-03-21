# -*- coding: utf-8 -*-


def main():
    import sys
    from math import pi

    input = sys.stdin.readline

    d = int(input())
    ans = (d / 2) ** 2 * pi
    print(ans)


if __name__ == "__main__":
    main()
