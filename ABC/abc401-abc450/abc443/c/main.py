# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, t = map(int, input().split())
    a = list(map(int, input().split())) + [t]
    time_open = 0
    ans = 0

    for ai in a:
        ans += max(0, ai - time_open)

        if ai > time_open:
            time_open = ai + 100

    print(ans)


if __name__ == "__main__":
    main()
