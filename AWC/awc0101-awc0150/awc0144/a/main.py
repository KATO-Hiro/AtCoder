# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    s = list(map(int, input().split()))
    l_min = min(l)
    ans = 0

    for si in s:
        if l_min >= si:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
