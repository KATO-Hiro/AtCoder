# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    ans = ""

    for _ in range(h):
        si = input().rstrip()

        if si.count("T") >= 1:
            ans += "o"
        else:
            ans += "x"

    print(ans)


if __name__ == "__main__":
    main()
