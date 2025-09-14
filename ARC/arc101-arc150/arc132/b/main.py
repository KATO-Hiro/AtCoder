# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    p = list(map(int, input().split()))

    for i, pi in enumerate(p):
        if pi != 1:
            continue

        if p[(i + 1) % n] == 2:
            ans = min(i, n - i + 1 + 1)
            print(ans)
            exit()
        else:
            ans = min(i + 1 + 1, n - i)
            print(ans)
            exit()


if __name__ == "__main__":
    main()
