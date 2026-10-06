# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    count, ans = -1, -1

    for i in range(h):
        si = input().rstrip()
        candidate = si.count(".")

        if candidate > count:
            count = candidate
            ans = i + 1

    print(ans)


if __name__ == "__main__":
    main()
