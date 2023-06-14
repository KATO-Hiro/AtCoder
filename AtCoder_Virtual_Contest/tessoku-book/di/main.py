# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    s = input().rstrip()
    on = s.count("1")
    off = s.count("0")
    ans = "No"

    if abs(k - on) % 2 == 0:
        if k > on and (k - on) <= off:
            ans = "Yes"
        elif k <= on:
            ans = "Yes"

    print(ans)


if __name__ == "__main__":
    main()
