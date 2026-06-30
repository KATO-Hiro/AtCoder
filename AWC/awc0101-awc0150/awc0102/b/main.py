# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    r = list(map(int, input().split()))
    s = list(map(int, input().split()))
    s_min = min(s)
    ans = 0

    for ri in r:
        if ri > s_min:
            continue

        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
