# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = list(map(int, input().split()))

    for _ in range(m):
        ti, pi = map(int, input().split())
        ti -= 1

        if pi > s[ti]:
            continue

        s[ti] -= pi

    ans = sum([1 for si in s if si == 0])
    print(ans)


if __name__ == "__main__":
    main()
