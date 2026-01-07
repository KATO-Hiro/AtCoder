# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = sorted(list(map(int, input().split())))
    x, y = a[-2], a[-1]
    ans1 = int("".join(map(str, [x, y])))
    ans2 = int("".join(map(str, [y, x])))
    print(max(ans1, ans2))


if __name__ == "__main__":
    main()
