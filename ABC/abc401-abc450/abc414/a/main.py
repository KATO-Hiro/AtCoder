# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, l, r = map(int, input().split())
    ans = 0

    for _ in range(n):
        xi, yi = map(int, input().split())

        if xi <= l and yi >= r:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
