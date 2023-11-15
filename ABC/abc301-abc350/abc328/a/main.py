# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    s = list(map(int, input().split()))
    ans = 0

    for si in s:
        if si <= x:
            ans += si

    print(ans)


if __name__ == "__main__":
    main()
