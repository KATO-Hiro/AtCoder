# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w, n = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    b = set([int(input()) for _ in range(n)])
    ans = 0

    for ai in a:
        count = 0

        for aij in ai:
            if aij in b:
                count += 1

        ans = max(ans, count)

    print(ans)


if __name__ == "__main__":
    main()
