# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, c = map(int, input().split())
    t = list(map(int, input().split()))
    prev = t[0]
    ans = 1

    for i, ti in enumerate(t):
        if i == 0:
            continue

        if ti - prev >= c:
            ans += 1
            prev = ti

    print(ans)


if __name__ == "__main__":
    main()
