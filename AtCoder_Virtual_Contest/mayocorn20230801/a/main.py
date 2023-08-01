# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = 0

    for k in range(1, 61):
        if 2**k <= n:
            ans = k
        else:
            break

    print(ans)


if __name__ == "__main__":
    main()
