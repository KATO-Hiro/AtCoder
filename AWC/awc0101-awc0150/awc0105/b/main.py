# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, p = map(int, input().split())
    s = list(map(int, input().split()))
    s.sort()
    ans = 0

    for si in s:
        if si > p:
            break

        p -= si
        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
