# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y, z = map(int, input().split())
    ans = abs(x)

    if x < y < z:
        if y < 0 < z:
            ans = abs(x) + 2 * abs(z)
    elif x < z < y:
        if y < 0:
            ans = -1
    elif y == min([x, y, z]):
        if 0 < y:
            ans = -1
    elif z < x < y:
        if y < 0:
            ans = -1
    elif z < y < x:
        if z < 0 < y:
            ans = abs(x) + 2 * abs(z)

    print(ans)


if __name__ == "__main__":
    main()
